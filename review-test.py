def calculate_price(price, discount):
    final_price = price - discount
    return final_price


def main():
    ticket_price = 5000
    discount = 500
    result = calculate_price(ticket_price, discount)
    print(result)


if __name__ == "__main__":
    main()
