from wallet_analyzer import analyze_wallet
from report_generator import generate_report

# Входные данные
wallet_address = "0xYourWalletAddressHere"

# Анализ кошелька
wallet_data = analyze_wallet(wallet_address)

# Генерация отчёта
generate_report(wallet_data)

print("✅ Анализ завершён! Отчёт сохранён в папке reports.")
