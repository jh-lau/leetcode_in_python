"""
  @Author       : liujianhan
  @Date         : 2020/7/14 上午9:58
  @Project      : leetcode_in_python
  @FileName     : 273.整数转换英文表示(H).py
  @Description  : 将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。
    示例 1:
    输入: 123
    输出: "One Hundred Twenty Three"
    示例 2:

    输入: 12345
    输出: "Twelve Thousand Three Hundred Forty Five"
    示例 3:

    输入: 1234567
    输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    示例 4:

    输入: 1234567891
    输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution:
    # 52ms, 13.8MB
    @staticmethod
    def number_to_words(num: int) -> str:
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result

    # 48ms, 13.6MB
    @staticmethod
    def number_to_words_v2(num: int) -> str:
        first = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        second = {20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
                  90: "Ninety"}

        def two(num):
            if num <= 19:
                return first[num]
            rest = num - num // 10 * 10
            if rest:
                return second[num // 10 * 10] + " " + first[rest]
            else:
                return second[num // 10 * 10]

        def three(num):
            hundred = num // 100
            unit = num - hundred * 100
            if hundred and unit:
                return first[hundred] + " Hundred " + two(unit)
            if hundred and not unit:
                return first[hundred] + " Hundred"
            return two(unit)

        if not num:
            return "Zero"
        res = ""
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        unit = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        if billion:
            res += three(billion) + " Billion"
        if million:
            if res:
                res += " " + three(million) + " Million"
            else:
                res += three(million) + " Million"
        if thousand:
            if res:
                res += " " + three(thousand) + " Thousand"
            else:
                res += three(thousand) + " Thousand"
        if unit:
            if res:
                res += " " + three(unit)
            else:
                res += three(unit)
        return res


if __name__ == '__main__':
    test_cases = [
        123, 12345, 1234567, 1234567891
    ]
    for tc in test_cases:
        print(Solution.number_to_words(tc))
        print(Solution.number_to_words_v2(tc))
