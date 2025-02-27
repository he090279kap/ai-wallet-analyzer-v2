from wallet_analyzer import analyze_wallet
from defi_analyzer import analyze_defi_activity
from nft_analyzer import analyze_nft_activity
from report_generator import generate_report

# Входные данные
wallet_address = "0xYourWalletAddressHere"

# Анализ кошелька
wallet_data = analyze_wallet(wallet_address)

# Анализ активности в DeFi
defi_data = analyze_defi_activity(wallet_address)

# Анализ NFT-транзакций
nft_data = analyze_nft_activity(wallet_address)

# Генерация отчёта
generate_report(wallet_data, defi_data, nft_data)

print("✅ Анализ завершён! Отчёт сохранён в папке reports.")
