#!/usr/bin/env python

from argparse import ArgumentParser
import sys
import time
import subprocess as subpro


class BudgetCalculator:

    category_list = {}
    income = 0
    total_percentage = 0
    title_string = ""
    def __init__(self, saveFile):
       self.file_name = "./saves/" + saveFile

    def calcuate_category(self, category_name):
        try:
            return self.income * (self.category_list[category_name]/100)
        except KeyError:
            return -1


    def start_week(self):
        subpro.call("clear")
        self.title_string = raw_input("Enter Week Title: ")
        for i in range(0, 10):
            if len(self.category_list) > 0:
                print "The following are the categories:\n"
                print "{}{:>20}{:>20}".format("#", "Name", "Percentage")
                cnt = 1
                for index in self.category_list:
                    print "{}){:>20}{:>20}".format(cnt, index, self.category_list[index]+"%")
                    cnt += 1
            cmd = raw_input("Enter one of the following command:\n{}\n{}\n:".format("a : Add new Category", "e : Done"))
            if cmd == "a":
                category_name = raw_input("Enter Category Name: ")
                category_percentage = raw_input("Enter {} Percentage: ".format(category_name.strip()))
                self.category_list[category_name] = category_percentage
                self.total_percentage += int(category_percentage)
            elif cmd == "e":
                break

        self.income = input("Enter this week's Income: ")


    def saveToFile(self):
        try:
            with open(self.file_name, "w") as f:
                f.write("$$TITLE$$;{};$$INCOME$$;{}\n".format(self.title_string,self.income))
                for key in self.category_list:
                    f.write(key + ";" + str(self.category_list[key]) + "\n")
            return 1
        except IOError:
            return -1


    def loadFromFile(self, filepath):
        try:
            with open(filepath, "r") as f:
                lines = f.readlines()
                headers = lines[0].strip().split(";")
                if headers[0] == "$$TITLE$$" and headers[2] == "$$INCOME$$":
                    self.title_string = headers[1]
                    self.income = headers[3]
                for lineIndex in range(1, len(lines)-1):
                    line = lines[lineIndex].strip().split(";")
                    self.category_list[line[0]] = line[1]
        except IOError:
            print "Failed to open file {}".format(filepath)
            return -1

    def weekly_budget_UI(self):
        subpro.call("clear")
        if len(self.title_string) > 1:
            print "Week Title: " + self.title_string
        else:
            print "No Week Loaded!"
        print "Please choose from the following commands:\n"
        print "{}: {}\n{}: {}\n{}: {}\n".format(
            "n",
            "New Week",
            "a",
            "Add Transaction",
            "l",
            "Load Saved File"
        )
        c = raw_input("Command: ")
        if c == "n":
            self.start_week()
        elif c == "s":
            self.saveToFile()
        elif c == "l":
            # path = input("Enter file name: ")
            path = "./saves/Test.txt"
            self.loadFromFile(path)




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
