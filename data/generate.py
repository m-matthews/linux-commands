# -*- coding: utf-8 -*-
# Copyright (C) 2020 Michael Matthews
#
#   This file is part of linux-commands.
#
#   linux-commands is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   linux-commands is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with linux-commands.  If not, see <http://www.gnu.org/licenses/>.

import os
import datetime
import random

def days_in_month(year, month):
    return (datetime.date(year, (month%12 + 1), 1) - datetime.timedelta(days=1)).day

if __name__=="__main__":
    print("Hello World")

    year=2019
    for state in ('NSW','ACT','VIC','QLD','SA','WA','TAS','NT'):
        with open("{}_combined.csv".format(state), "w") as f1:
            print("state,date,value", file=f1)
            for month in range(1,13):
                with open("{}_{}-{:02d}.csv".format(state, year, month), "w") as f2:
                    print("state,date,value", file=f2)
                    for day in range(1, days_in_month(year, month)+1):
                        for f in (f1, f2):
                            print("{},{},{}".format(state,
                                                    datetime.date(year,month,day).strftime("%Y/%m/%d"),
                                                    random.randint(1000,100000)), file=f)
