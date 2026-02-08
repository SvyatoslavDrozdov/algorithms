HIGHEST_PRICE_OF_LUNCH: int = 300
MAX_DAYS_COUNT: int = 100
COUPON_THRESHOLD: int = 100
INF: int = HIGHEST_PRICE_OF_LUNCH * MAX_DAYS_COUNT + 1


def calculate_dp_list(cost_of_lunches: list[int]) -> list[list[int]]:
    days_count: int = len(cost_of_lunches)
    padded_cost_of_lunches: list[int] = [INF] + cost_of_lunches
    dp: list[list[int]] = [[INF] * (days_count + 1) for _ in range(days_count + 2)]
    dp[0][0] = 0
    for day_number in range(1, days_count + 1):
        for coupon in range(days_count + 1):
            if padded_cost_of_lunches[day_number] > COUPON_THRESHOLD:
                paid_lunch: int = dp[coupon - 1][day_number - 1] + padded_cost_of_lunches[day_number]
            else:
                paid_lunch: int = dp[coupon][day_number - 1] + padded_cost_of_lunches[day_number]

            coupon_lunch: int = dp[coupon + 1][day_number - 1]
            dp[coupon][day_number] = min(paid_lunch, coupon_lunch)

    return dp


def calculate_best_price_and_coupons_info(cost_of_lunches: list[int]) -> tuple[int, int, list[int]]:
    dp: list[list[int]] = calculate_dp_list(cost_of_lunches)
    days_count: int = len(dp[0]) - 1

    coupons: int = days_count
    best_price: int = INF
    best_remaining_coupons: int = coupons

    while coupons >= 0:
        if best_price > dp[coupons][days_count]:
            best_price = dp[coupons][days_count]
            best_remaining_coupons = coupons
        coupons -= 1

    days_to_use_coupons: list[int] = []
    current_coupons: int = best_remaining_coupons
    padded_cost_of_lunches: list[int] = [INF] + cost_of_lunches
    for day_number in range(days_count, 0, -1):
        if dp[current_coupons + 1][day_number - 1] == dp[current_coupons][day_number]:
            days_to_use_coupons.append(day_number)
            current_coupons += 1
        elif padded_cost_of_lunches[day_number] > COUPON_THRESHOLD:
            current_coupons -= 1

    return best_price, best_remaining_coupons, days_to_use_coupons[::-1]


def main() -> None:
    days_count: int = int(input())
    cost_of_lunches: list[int] = []
    for _ in range(days_count):
        cost_of_lunches.append(int(input()))

    best_price, best_remaining_coupons, days_to_use_coupons = calculate_best_price_and_coupons_info(cost_of_lunches)
    used_coupons: int = len(days_to_use_coupons)
    print(best_price)
    print(best_remaining_coupons, used_coupons)
    print(*days_to_use_coupons)


if __name__ == "__main__":
    main()
