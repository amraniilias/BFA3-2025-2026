def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return avrage


def main():
    nums = [10, 20, 30, 40, 50]
    print("Numbers:", nums)

    result = calculate_average(nums)
    print("The average is:", result)

    nums = [10, 20, 30, 40, 't']
    print("Numbers:", nums)

    result = calculate_average(nums)
    print("The average is:", result)

if __name__ == "__main__":
    main()