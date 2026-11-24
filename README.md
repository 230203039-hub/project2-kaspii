# Kaspi.kz seller delivery tariff impact
Study model: compare the February 2025 and January 2026 tariff schedules on the same simulated orders dated February–June 2026. This is a counterfactual scenario, not observed year-over-year data. All values exclude VAT; contribution profit excludes overhead, returns and tax. The commission is assumed at 10%, not an official rate.

Process: order -> seller packs -> delivery -> customer receives -> delivery fee deducted [cost bottleneck] -> seller contribution profit.
Possible causes: new fees on low-value orders; route-specific tariff differences; product acquisition costs; platform commission. Focus on the first two while holding other costs constant.

Run `pip install numpy pandas scipy` then `python analysis.py` to regenerate raw and clean CSVs and both Welch tests. Seed 42. Raw 1515 rows; clean 1500 rows, 14 columns. Normalize route case before removing 15 duplicate records. No missing values; price, weight and cost ranges checked; no outliers removed. The tests measure simulated tariff effects only; p-values cannot establish real seller outcomes. No personal data.

Sources (accessed 2026-11-25; tariff values transcribed, no source files downloaded):
- https://guide.kaspi.kz/cdn/content/pay/Informatsiya-o-stoimosti-uslug-k-dogovoru-s-Kaspi-Magazinom-Kaspi-Dostavka.pdf?ri=d7585bf3-d059-4a93-a78a-6af873f823b6 (2025 schedule)
- https://guide.kaspi.kz/partner/ru/shop/delivery/shipping/q2288 (2026 schedule and deductions)
- https://guide.kaspi.kz/cdn/content/pay/product/documents/Magazin/stoimost-servisa-kaspi-dostavka-s-1-1-2026.pdf?ri=c83b8b14-612d-4aab-908c-44648aa9eb51 (exact 2026 fees)
- https://invoices.kz/guides/tarify-dostavki-kaspi-magazin (external corroboration)
- https://raystone.kz/kaspi/dostavka (external corroboration)
