## three events sampled from U(0, 1)
# need a strategy to get the highest score expected scored long term
#
# for a given value A, probability of a sampled value (x) being less than A is A, being more than A is 1-A
#
# Bayes theorem = P(A | B) = P(A&B) / P(B)
#
# first value drawn is x0
#
#

# Example of how to think of these conditional probabilities given a uniform distribution
#        p (x > .4 & x > .3 | .4 > .3) = p(x > .4 | .4 > .3) = p(x > .4) =  .6
#        p (x < .4 & x > .3 | .4 > .3) = p(x between .4 and .3 | .4 > .3) = p(x between .4 and .3) = .4 - .3 = .1
#        p (x < .4 & x < .3 | .4 > .3) = p(x < .3 | .4 > .3) = p(x < .3) =  .3
#
# p(1,2,3)
#       p(x1 > x0) * p(x2 > x1 & x2  > x0| x1 > x0)
#       p(x1 > x0) * p(x2 > x1 | x1 > x0)
#       = (1-x0) * (1-x1)

# p(1,3,2)
#       p(x1 > x0) * p(x2 > x0 & x2 < x1 | x1 > x0)
#       p(x1 > x0) * p(x2 is between x0 and x1 | x1 > x0)
#       = (1 - x0) * (x1 - x0)

# p(2, 1, 3)
#       p(x1 < x0) * p(x2 > x0 and x2 > x1 | x1 < x0)
#       p(x1 < x0) * p(x2 > x0| x1 < x0)
#       = x0 * (1-x0)

# p(2, 3, 1)
#       p(x1 > x0) * p(x2 < x1 and x2 < x0 | x1 > x0)
#       p(x1 > x0) * p(x2 < x0 | x1 > x0)
#       = (1 - x0) * x0

# p(3, 1, 2)
#       p(x1 < x0) * p(x2 < x0 & x2 > x1 | x1 < x0)
#       p(x1 < x0) * p(x2 is between x0 and x1 | x1 < x0)
#       = x0 * (x0 - x1)

# p(3, 2, 1)
#       p(x1 < x0) * p(x2 < x1 and x2 < x0| x1 < x0)
#       p(x1 < x0) * p(x2 < x1 | x1 < x0)
#       = x0 * x1

# Probability of successes if you pick X initially:
#   P(success | pick 1):
#       p(1,2,3) + p(1,3,2)
#       (1-x0)*(1-x1) + (1-x0) * (x1-x0)
#       (1-x0)*(1-x1) + (1-x0)*x1 + (1-x0)*-x0
#       (1-x0)*(1-x1 + x1) + -x0 + x0^2
#       1 - 2*x0 + x0^2
#       (1-x0)^2
#
#   P(success | pick 2):
#       p(2,1,3) + p(2,3,1)
#       2 * (1-x0) * x0
#       2*x0 - 2*(x0^2)
#
#   P(success | pick 3):
#       p(3,1,2) + p(3,2,1)
#       x0 * (x0 - x1) + x0*x1
#       x0^2 - x0*x1 + x0*x1
#       x0^2
#
# If you find where the these values are equal to each other you find that
# the decision boundaries for x0 is 1/3 and 2/3. Anything below should get
# a one chosen, anything in between should get 2 chosen and anything above
# should get three chosen


def game(N, get_next_x, submit_rank):
    # This is the winning strategy for N=2.
    # Write code that works for N=2, N=3
    if N == 2:
        x0 = get_next_x()
        if x0 < 0.5:
            submit_rank(1)
            get_next_x()
            submit_rank(2)
        else:
            submit_rank(2)
            get_next_x()
            submit_rank(1)
    if N == 3:
        x0 = get_next_x()

        prob_for_1 = (1-x0)**2
        prob_for_2 = (1-x0)*x0
        prob_for_3 = x0**2
        print('probs', prob_for_1, prob_for_2, prob_for_3)

        # probabilty below which it makes more sense to guess 1
        if x0 <= 0.33333333:
            submit_rank(1)
            x1 = get_next_x()
            print(x0, x1)

            # probability next one is a 3 vs prob next one is a 2
            if (1-x1) > (x1 - x0):
                submit_rank(2)
                print(get_next_x())
                submit_rank(3)
            else:
                submit_rank(3)
                print(get_next_x())
                submit_rank(2)

        # probability above which it makes sense to guess 3
        elif x0 >= .666666:
            submit_rank(3)
            x1 = get_next_x()
            print(x0, x1)

            # probability next one is a 2 vs prob next one is a 1
            if (x0 - x1) > x1:
                submit_rank(1)
                print(get_next_x())
                submit_rank(2)
            else:
                submit_rank(2)
                print(get_next_x())
                submit_rank(1)

        else:
            submit_rank(2)
            x1 = get_next_x()
            print(x0, x1)

            if x1 > x0:
                submit_rank(3)
                print(get_next_x())
                submit_rank(1)
            else:
                submit_rank(1)
                print(get_next_x())
                submit_rank(3)


