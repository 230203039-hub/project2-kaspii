import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from pathlib import Path
P=Path(__file__).parent
rng=np.random.default_rng(42)
n=1500
# Hypotheses specified before simulation: H1a low orders have larger percentage-point loss than mid-price orders; H1b city and express differ for high-value orders.
band=rng.choice(['low','mid','high'],n)
price=np.array([rng.integers(*{'low':(1100,4900),'mid':(5100,9900),'high':(16000,40000)}[b]) for b in band])
route=rng.choice(['city','national','express'],n)
weight=np.round(rng.uniform(.2,4.8,n),2)
cat=rng.choice(['home','electronics','accessories'],n)
cost=np.round(price*rng.uniform(.55,.80,n),2)
commission=np.round(price*.10,2)
old=np.array([0 if b=='low' else ({'city':699,'national':799,'express':799}[r] if b=='mid' else {'city':799,'national':1299,'express':1499}[r]) for b,r in zip(band,route)])
new=np.array([149.14 if p<3000 else 199.14 if b=='low' else {'city':699.14,'national':799.14,'express':799.14}[r] if b=='mid' else {'city':1099.14,'national':1299.14,'express':1699.14}[r] for p,b,r in zip(price,band,route)])
d=pd.DataFrame(dict(order_id=np.arange(1,n+1),date=pd.Timestamp('2026-02-01')+pd.to_timedelta(rng.integers(0,150,n),unit='D'),category=cat,band=band,route=route,price_kzt=price,weight_kg=weight,product_cost_kzt=cost,commission_kzt=commission,fee_2025_kzt=old,fee_2026_kzt=new))
raw=pd.concat([d,d.iloc[:15]],ignore_index=True); raw.loc[:20,'route']=raw.loc[:20,'route'].str.upper();raw.to_csv(P/'data_raw.csv',index=False)
c=pd.read_csv(P/'data_raw.csv',parse_dates=['date']); c['route']=c.route.str.lower().str.strip();c=c.drop_duplicates();assert c.order_id.is_unique and not c.isna().any().any() and c.weight_kg.between(.2,4.8).all() and c.price_kzt.between(1100,40000).all() and (c.product_cost_kzt<c.price_kzt).all()
for y in [2025,2026]: c[f'profit_{y}_kzt']=(c.price_kzt-c.product_cost_kzt-c.commission_kzt-c[f'fee_{y}_kzt']).round(2)
c['loss_pp']=((c.profit_2025_kzt-c.profit_2026_kzt)/c.price_kzt*100).round(5)
c.to_csv(P/'data_clean.csv',index=False)
for name,a,b in [('H1a',c[c.band=='low'].loss_pp,c[c.band=='mid'].loss_pp),('H1b',c[(c.band=='high')&(c.route=='city')].loss_pp,c[(c.band=='high')&(c.route=='express')].loss_pp)]:
 t,p=ttest_ind(a,b,equal_var=False,alternative='greater' if name=='H1a' else 'two-sided'); print(name,len(a),len(b),a.mean(),b.mean(),t,p)
print(c.groupby('band').loss_pp.mean())
