"""
PRACTICE Test 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in 2D GRAPHICS problems.  ***

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathaniel Blanco.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 2 question.
#     5 is a "typical" Test 2 question.
#     7 is a "hard" Test 2 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
########################################################################

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_hourglass()
    run_test_many_hourglasses()


def run_test_hourglass():
    """ Tests the    hourglass    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   hourglass   function:')
    print('--------------------------------------------------')

    test1 = '(n = 3, radius = 40, blue)'
    test2 = '(n = 8, radius = 15, green)'
    title1 = 'Hourglass, two tests: {} and {}'.format(test1, test2)
    window1 = rg.RoseWindow(600, 500, title1)

    hourglass(window1, 3, rg.Point(150, 200), 40, 'blue')
    hourglass(window1, 8, rg.Point(450, 250), 15, 'green')

    window1.close_on_mouse_click()

    test3 = '(n = 6, radius = 30, red)'
    title2 = 'Hourglass, one more test: {}'.format(test3)
    window2 = rg.RoseWindow(400, 700, title2)

    hourglass(window2, 6, rg.Point(200, 350), 30, 'red')

    window2.close_on_mouse_click()


def hourglass(window, n, point, radius, color):
    """
    See   hourglass_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Displays an "hourglass" shape of circles in the given window.
      -- Each circle has the given radius and given color.
      -- Each circle has a horizontal line drawn through it.
      -- The middlemost of the circles is centered at the given point.
      -- There is a single circle in that middlemost row.
      -- There are n rows (including the middlemost row)
            of circles going UP from the middlemost circle.
      -- There are n rows (including the middlemost row)
           of circles going DOWN from the middlemost circle.
      -- Each circle barely touches its neighbor circles.

    Preconditions:
      :type window: rg.RoseWindow
      :type n: int
      :type point: rg.Point
      :type radius: int
      :type color: str
    where n and radius are positive and color is a string that denotes
    a color that rosegraphics understands.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #       We provided some tests for you (above).
    # ------------------------------------------------------------------
    ####################################################################
    # BONUS: Avoid replicated code if you can.  Hint: You are allowed
    #        to define an additional function(s) if you wish.
    ####################################################################
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      8
    #    TIME ESTIMATE:  25 minutes (warning: this problem is challenging)
    # ------------------------------------------------------------------
    rad = radius
    diameter = rad * 2
    center = point
    circle = rg.Circle(center, rad)
    circle.fill_color = color

    line = rg.Line(rg.Point(center.x - rad, center.y), rg.Point(center.x + rad, center.y))
    circle.attach_to(window)
    line.attach_to(window)

    for row in range(1, n):

        circle_upper = circle.clone()
        circle_upper.center.x = center.x - (diameter / 2) * row
        circle_upper.center.y = center.y + ((diameter ** 2 - rad ** 2) ** (1 / 2)) * row
        circle_upper.fill_color = color
        line1 = rg.Line(rg.Point(circle_upper.center.x - rad, circle_upper.center.y),
                        rg.Point(circle_upper.center.x + rad, circle_upper.center.y))

        circle_lower = circle.clone()
        circle_lower.center.x = center.x - (diameter / 2) * row
        circle_lower.center.y = center.y - ((diameter ** 2 - rad ** 2) ** (1 / 2)) * row
        circle_lower.fill_color = color
        line2 = rg.Line(rg.Point(circle_lower.center.x - rad, circle_lower.center.y),
                        rg.Point(circle_lower.center.x + rad, circle_lower.center.y))

        circle_upper.attach_to(window)
        circle_lower.attach_to(window)
        line1.attach_to(window)
        line2.attach_to(window)

        for number_of_circles in range(row):

            circle_in_upper_row = circle_upper.clone()
            circle_in_upper_row.center.x = circle_upper.center.x + diameter * (number_of_circles + 1)
            circle_in_upper_row.fill_color = color
            line1 = rg.Line(rg.Point(circle_in_upper_row.center.x - rad, circle_in_upper_row.center.y),
                            rg.Point(circle_in_upper_row.center.x + rad, circle_in_upper_row.center.y))

            circle_in_lower_row = circle_lower.clone()
            circle_in_lower_row.center.x = circle_lower.center.x + diameter * (number_of_circles + 1)
            circle_in_lower_row.fill_color = color
            line2 = rg.Line(rg.Point(circle_in_lower_row.center.x - rad, circle_in_lower_row.center.y),
                            rg.Point(circle_in_lower_row.center.x + rad, circle_in_lower_row.center.y))

            circle_in_upper_row.attach_to(window)
            circle_in_lower_row.attach_to(window)
            line1.attach_to(window)
            line2.attach_to(window)

    window.render()


def run_test_many_hourglasses():
    """ Tests the    many_hourglasses    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   many_hourglasses   function:')
    print('--------------------------------------------------')

    test1 = '(n = 4, radius = 30, red-blue-black-green)'
    test2 = '(n = 3, radius = 70, brown-cyan-yellow-green)'
    title1 = 'Many hourglasses, two tests: {} and {}'.format(test1,
                                                             test2)
    window1 = rg.RoseWindow(800, 400, title1)

    square1 = rg.Square(rg.Point(50, 150), 30)
    square2 = rg.Square(rg.Point(400, 200), 70)

    many_hourglasses(window1, square1, 4,
                     ('red', 'blue', 'black', 'green'))
    many_hourglasses(window1, square2, 3,
                     ('brown', 'cyan', 'yellow', 'green'))
    window1.close_on_mouse_click()

    test3 = '(n = 7, radius = 40, red-black-blue)'
    title2 = 'Many hourglasses, one more test: {}'.format(test3)
    window2 = rg.RoseWindow(1200, 500, title2)

    square3 = rg.Square(rg.Point(50, 250), 40)

    many_hourglasses(window2, square3, 7, ('red', 'black', 'blue'))

    window2.close_on_mouse_click()


def many_hourglasses(window, square, m, colors):
    """
    See   many_hourglasses_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Displays  m  rectangles, where:
      -- Each rectangle has an hourglass of circles inside it,
           per the  hourglass  function above.
      -- The circles in the hourglasses are all the same size.
      -- The leftmost rectangle is the given square, and it contains
           an hourglass with a single circle that fills the square.
      -- Each successive rectangle is immediately to the right of the
           previous rectangle, and each contains an hourglass with
           the hourglass'  n   being one greater than the  n  used
           for the previous rectangle.
      -- The colors for the hourglass figures use the given sequence of
           colors, "wrapping" if m exceeds the length of the sequence.

    Preconditions:
      :type window: rg.RoseWindow
      :type square: rg.Square
      :type m: int
      :type colors: (list | tuple) of str
    where m is positive and colors is a sequence of strings,
    each of which denotes a color that rosegraphics understands.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #       We provided some tests for you (above).
    # ------------------------------------------------------------------
    ####################################################################
    # IMPORTANT:
    #   1. Partial credit if you draw JUST the rectangles.
    #   2. No additional credit unless you CALL the  hourglass  function
    #        in the PREVIOUS problem appropriately
    #        to draw the hourglass figures.
    ####################################################################
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7  (assuming that you already have
    #                         a correct "hourglass" function above)
    #    TIME ESTIMATE:  20 minutes (warning: this problem is challenging)
    # ------------------------------------------------------------------
    counter = 0
    for rectangle_iteration in range(m):

        # Rectangle's width will be the circle's diameter plus another diameter
        # for every additional row of the hourglass
        # width = n * diameter
        # Rectangle's height will be the circle's radius plus root 3 radius (Pythagorean theorem)
        # for every additional row of the hourglass, multiplied by two

        diameter = square.length_of_each_side

        # These loops determine how far to move to the right for both corners
        amount_of_diameters_1 = 0
        amount_of_diameters_2 = 0
        for rectangle_number in range(1, rectangle_iteration + 1):
            amount_of_diameters_1 = amount_of_diameters_1 + rectangle_number

        for rectangle_number in range(2, rectangle_iteration + 2):
            amount_of_diameters_2 = amount_of_diameters_2 + rectangle_number

        # Constructing the rectangle
        corner_1 = rg.Point(square.center.x - diameter / 2 + amount_of_diameters_1 * diameter,
                            square.center.y - (3 ** (1/2)) * (diameter / 2) * rectangle_iteration - (diameter / 2))
        corner_2 = rg.Point(square.center.x + diameter / 2 + amount_of_diameters_2 * diameter,
                            square.center.y + (3 ** (1/2)) * (diameter / 2) * rectangle_iteration + (diameter / 2))
        rectangle = rg.Rectangle(corner_1, corner_2)
        rectangle.attach_to(window)

        # Determining the current color
        color = colors[counter]
        if counter == len(colors) - 1:
            counter = 0
        else:
            counter = counter + 1

        # Constructing the hourglass
        hourglass(window, rectangle_iteration + 1, rectangle.get_center(), diameter / 2, color)

        window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
