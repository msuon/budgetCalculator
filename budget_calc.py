#!/usr/bin/env python

from argparse import ArgumentParser
import sys
import time
import subprocess as subpro


class BudgetCalculator:

    category_list = [("Name","Percentage")]
    income = 0
    total_percentage = 0
    def __init__(self, saveFile):
       self.file_name = saveFile

    def calcuate_category(self, category_name):
        for each in self.category_list:
            if each[0] == category_name:
                return (each[1]/100) * self.income

        return -1

    def start_week(self):
        subpro.call("clear")
        for i in range(0, 10):
            if len(self.category_list) > 1:
                print "The following are the categories:\n"
                for index in range(0, len(self.category_list)):
                    print "{}){:^20}{:^20}".format(index, self.category_list[index][0], self.category_list[index][1])
            cmd = raw_input("Enter one of the following command:\n{}\n{}".format("a : Add new Category", "e : Done"))
            if cmd == "a":
                category_name = raw_input("Enter Category Name: ")
                category_percentage = raw_input("Enter {} Percentage: ".format(category_name.strip()))
                self.category_list.append((category_name,category_percentage))
                self.total_percentage += category_percentage
            elif cmd == "e":
                break

        self.income = input("Enter this week's Income: ")






    def weekly_budget_UI(self):
        print "Please choose from the following commands:\n"
        print "{}: {}\n{}: {}\n".format("n", "New week", "a", "Add transaction")
        c = raw_input("Command: ")
        if c == "n":
            self.start_week()


if __name__ == "__main__":

    calc = BudgetCalculator("Test.txt")
    if len(sys.argv) > 1:
        parser = ArgumentParser(description="Calculate weekly budget.")
        parser.add_argument("-i", action="store", type=float, required=False, help="The amount of income this week.")
        parser.add_argument("-l", action="store", type=float, required=False, default=0.15, help="Percentage of leisure fund.")
        parser.add_argument("-t", action="store", type=float, required=False, default=0.05, help="Percentage of turtle fund.")
        parser.add_argument("-r", action="store", type=float, required=False, default=0.30, help="Percentage for rent.")
        args = parser.parse_args()
    else:
        print "Budget Calculator(Interactive Mode)"
        while True:
            calc.weekly_budget_UI()


    # l_fund = args.l * args.i
    # t_fund = args.t * args.i
    # r_fund = args.r * args.i
    # savings = args.i - (l_fund + t_fund + r_fund)
    #
    # if args.weekly_budget_mode:
    #     weekly_budget_UI()
    #
    # print "This week's income: ${0}".format(args.i)
    # print "This week's leisure fund: ${0}".format(l_fund)
    # print "This week's turtle fund: ${0}".format(t_fund)
    # print "This week's rent fund: ${0}".format(r_fund)
    # print "This week's savings fund: ${0}".format(savings)
