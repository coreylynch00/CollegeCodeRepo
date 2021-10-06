# Rugby Score Calculator
# Author: Corey Lynch
# Date: 26/09/2019

goal_points = 3
penalty_points = 3
tries_points = 5
conversion_points = 2

goals_england = int(input('How many goals did England score?'))
penalty_england = int(input('How many penalties did England score?'))
tries_england = int(input('How many tries did England score?'))
conversion_england = int(input('How many conversions did England make?'))

goals_irl = int(input('How many goals did Ireland score?'))
penalty_irl = int(input('How many penalties did Ireland score?'))
tries_irl = int(input('How tries did Ireland score?'))
conversion_irl = int(input('How many conversions did Ireland make?'))

total_points_england = goals_england * goal_points + penalty_england * penalty_points + tries_england * \
                       tries_points + conversion_england * conversion_points

total_points_irl = goals_irl * goal_points + penalty_irl * penalty_points + tries_irl * tries_points \
                   + conversion_irl * conversion_points

print('The over all result of the match was', total_points_england, 'points to England,',
      total_points_irl, 'points to Ireland')
