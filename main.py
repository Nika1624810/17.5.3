from collections import defaultdict
from json import load


def main():
    with open('orders_july_2023.json', 'r', encoding='UTF-8') as file:
        orders = load(file)

        # 1. Самый дорогой заказ
        most_expensive_order_id = None
        most_expensive_order_cost = 0

        # 2. Заказ с наибольшим количеством товаров
        biggest_quantity_order_id = None
        biggest_quantity_value = 0

        # 3. Количество заказов по дням
        orders_per_day = defaultdict(int)

        # 4. Количество заказов по пользователям
        user_order_count = defaultdict(int)

        # 5. Сумма заказов по пользователям
        user_order_sum = defaultdict(int)

        # 6. Средняя стоимость заказа
        total_order_sum = 0
        total_order_count = len(orders)

        # 7. Средняя стоимость товаров
        total_product_sum = 0
        total_product_count = 0

        for order_id, order_data in orders.items():
            price = order_data['price']
            quantity = order_data['quantity']
            user_id = order_data['user_id']
            date = order_data['date']
            # 1
            if price > most_expensive_order_cost:
                most_expensive_order_id = order_id
                most_expensive_order_cost = price
            # 2
            if quantity > biggest_quantity_value:
                biggest_quantity_order_id = order_id
                biggest_quantity_value = quantity
            # 3
            orders_per_day[date] += 1
            # 4
            user_order_count[user_id] += 1
            # 5
            user_order_sum[user_id] += price
            # 6
            total_order_sum += price
            # 7
            total_product_sum += price
            total_product_count += quantity

        # 3. День с наибольшим количеством заказов
        busiest_day, max_orders_per_day = max(orders_per_day.items(), key=lambda x: x[1])

        # 4. Пользователь с наибольшим количеством заказов
        top_user_by_count, max_user_order_count = max(user_order_count.items(), key=lambda x: x[1])

        # 5. Пользователь с наибольшей суммой заказов
        top_user_by_sum, max_user_order_sum = max(user_order_sum.items(), key=lambda x: x[1])

        # 6. Средняя стоимость заказа
        average_order_cost = round(total_order_sum / total_order_count, 2)

        # 7. Средняя стоимость товаров
        average_product_cost = round(total_product_sum / total_product_count, 2)

        print(
            "Результаты:\n"
            f"1) Самый дорогой заказ {most_expensive_order_id} ({most_expensive_order_cost} руб.)\n"
            f"2) Заказ с наибольшим количеством товаров {biggest_quantity_order_id} ({biggest_quantity_value} шт.)\n"
            f"3) День с наибольшим количеством заказов {busiest_day} ({max_orders_per_day})\n"
            f"4) Пользователь с наибольшим количеством заказов {top_user_by_count} ({max_user_order_count})\n"
            f"5) Пользователь с наибольшей суммой заказов {top_user_by_sum} ({max_user_order_sum} руб.)\n"
            f"6) Средняя стоимость заказа {average_order_cost} руб.\n"
            f"7) Средняя стоимость товаров {average_product_cost} руб."
        )

if __name__ == '__main__':
    main()
