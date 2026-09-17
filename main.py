def convert_currency(amount, rate):
    return amount * rate

def main():
    print("=== Simple Currency Converter ===")
    
    # Фиксированные базовые курсы (к USD)
    rates = {
        "EUR": 0.92,
        "KZT": 475.0,
        "RUB": 88.5,
        "BTC": 0.000015
    }

    try:
        usd_amount = float(input("Введите сумму в USD: "))
        if usd_amount < 0:
            print("Сумма должна быть положительной.")
            return

        print(f"\nЭквивалент для {usd_amount} USD:")
        print("---------------------------")
        for currency, rate in rates.items():
            converted = convert_currency(usd_amount, rate)
            if currency == "BTC":
                print(f"• {currency}: {converted:.6f}")
            else:
                print(f"• {currency}: {converted:.2f}")
        print("---------------------------")

    except ValueError:
        print("Ошибка: Введите корректное число.")

if __name__ == "__main__":
    main()