'''
HackerLand Enterprise is adopting a new viral advertising strategy. When they
launch a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those 5 people (i.e., floor(5/2) = 2) like the
advertisement and each shares it with 3 of their friends. At the beginning of
the second day, floor(5/2) * 3 = 2 * 3 = 6 people receive the advertisement.

Each day, floor(recipients/2) of the recipients like the advertisement and will
share it with 3 friends on the following day. Assuming nobody receives the
advertisement twice, determine how many people have liked the ad by the end of
a given day, beginning with launch day as day 1.

For example, assume you want to know how many have liked the ad by the end of
the 5-th day.

Day Shared Liked Cumulative
1      5     2       2
2      6     3       5
3      9     4       9
4     12     6      15
5     18     9      24
The cumulative number of likes is 24.

Input Format
A single integer, n, denoting a number of days.

Constraints
1 <= n <= 50

Output Format
Print the number of people who liked the advertisement during the first n days.

Sample Input
3

Sample Output
9

Explanation
2 people liked the advertisement on the first day, 3 people liked the
advertisement on the second day and 4 people liked the advertisement on the
third day, so the answer is 2 + 3 + 4 = 9.
'''


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    people_count = 5
    result = 0
    for _ in range(n):
        result += people_count // 2
        people_count = people_count // 2 * 3
        # print(result)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # result = viralAdvertising(n)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    result = viralAdvertising(0)
    print(result)  # 0

    result = viralAdvertising(1)
    print(result)  # 2

    result = viralAdvertising(2)
    print(result)  # 5

    result = viralAdvertising(3)
    print(result)  # 9

    result = viralAdvertising(4)
    print(result)  # 15

    result = viralAdvertising(5)
    print(result)  # 24

    result = viralAdvertising(50)
    print(result)  # 2068789129