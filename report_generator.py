import pdfkit

def generate_report(wallet_data):
    report_md = f"# Анализ кошелька {wallet_data['wallet_address']}\n\n"
    
    report_md += "## Ethereum Транзакции:\n"
    for tx in wallet_data["eth_transactions"][:5]:
        report_md += f"- Hash: {tx['hash']}, Value: {tx['value']} ETH\n"

    report_md += "## Solana Транзакции:\n"
    for tx in wallet_data["sol_transactions"][:5]:
        report_md += f"- Signature: {tx['signature']}, Amount: {tx['amount']} SOL\n"

    # Сохранение в Markdown
    with open("reports/wallet_report.md", "w", encoding="utf-8") as f:
        f.write(report_md)

    # Конвертация в PDF
    pdfkit.from_file("reports/wallet_report.md", "reports/wallet_report.pdf")
