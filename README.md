# MAGIC SQUARES IN PYTHON
#### Video Demo: [YouTube](https://youtu.be/K39YhJRyPWY)
#### Description:

This is a brief synopsis and explanation of my final project for CS50P,
entitled Magic Squares in Python. A regular Magic Square is an n * n square, filled with numbers
from 1 to n squared. the goal is for the sum of each row, column, and diagonal to equal the same magic
number, which can be calculated with (n * (squared + 1)) // 2. By placing the right numbers into the right
cells, this can be achieved.

My first step was to try an simply generate random orders of the numbers into squares, and
waiting until a magic square was returned. to do this I created a NumPy array and placed the the numbers randomly inside,
then checked the result with a custom function. If the result was not magic, the program would simply continue
to infinitely generate squares with a "while" loop. However, once I realized that based on the factorial of whatever
n would be (n!), I'd probably be waiting for far longer than I had thought. My next step was to add several steps to try
and limit the randomness of the program. After several tweaks, I was able to generate a square of n=3 instantaneously, but
for n=4 it still took several minutes to run through all the possible squares before hitting the right one, and by n=5
the factorial became so astronomically high that even when I let the program run for more than 24 hours at a time, going through
millions of iterations in the process, it was still unable to generate a 5 by 5 magic square. I had to find a better
solution.

After doing some research, I found three algorithms capable of easily generating magic squares of any size. All three
were necessary, beacuse the process of creating a magic square depended on the type of integer n was, be it odd, doubly
even (divisible by 4 as well as 2), or singly even (only divisible by 2). The three methods were as follows:

-** The Siamese Method: (For odd numbered squares)
            The Siamese Method is an elegant way to create a magic square where n is odd, no matter
            the size. The process is simple: First, 1 is placed in the center cell of the top row of
            the square. You then move up and to the right, with wrapping, so if you're on the top row
            the next number will be on the bottom row, and if you're in the rightmost row the next
            number will be on the leftmost column. The next number is then placed in this new cell.
            If going up and to the right lands in a square that had been previously filled, you
            instead return to the previous square (the one that had been filled most recently), and go down
            one cell from there, again with wrapping. This process is then continued, with each number being
            placed in a cell in turn until the entire square has been filled. The result will be an odd-ordered
            magic square.

-** Strachey's Method: (For singly even squares)
            For squares in which n is singly even, meaning it is divisible by 2 but not by 4, Strachey's method
            is a somewhat complicated yet precise algorithm which yields consistent results. First, an empty
            square of n by n size is created. This is then split into four subsquares each of which will have
            an odd number of cells. A square of n=10 for example, will be split into four smaller squares, each
            of which will be in itself a 5 by 5 square. These are labeled, starting from top left and moving
            horizontally, "A", "C", "D", and "B". In alphabetical order, each square is then filled using the Siamese
            Method, albeit with different numbers. The list of numbers from 1 to n squared is then also split into
            four parts, and each square, in alphabetical order, is filled with these sublists, with "A" getting all
            the numbers from 1 to (n squared / 4) and so on. Several operations are then performed. First, the leftmost
            'k' columns (where k is (n - 2) / 4) in subsquare "A" are interchanged with the same in subsquare "D".
            Next, the rightmost k - 1 columns in subsquare "C" are interchanged with the same in subsquare "B". If
            k - 1 = 0, as it does where n=6, this operation is not performed. The center square of "A" is then
            interchanged with the same in "D", and the values of the middle cells of the first columns in "A" and
            "D" are swapped as well. This results in a magic square of singly-even order.

-** The Generic Method: (For doubly even squares)
            The Generic Method is a rather simple yet effective method of creating doubly even magic squares. Fist,
            a square of n by n size is created, divided into (n / 4) * (n / 4) subsquares. These all retain their
            positions within the original n by n square. The original square is then filled sequentially, from top
            left and moving horizontally, beginning from 1. This will output a n by n square where every celled is
            filled with successive numbers from 1 to n squared. Lastly, any number that is not on either diagonal
            within their respective subsquares is replaced by the number ((squared + 1) - {whatever number was in the cell}),
            which will obviously be a different number for each cell. The result will be a doubly even magic square.


These processes were implemented in my code as follows:

-** The main() function began by calling a function called simply get_n(). This prompted the user to enter the size of the desired
square. Functionality was added to ensure that the input would only accept a valid response. Given that the lowest number with which
a magic square is possible is 3, if the user entered 1 or 2 they would simply be given a message explaining why their input was being
rejected, and be prompted to enter another value, thanks to a simple "while" loop. This would happen as well if the user were simply
to enter anything that wasn't an integer, or if nothing at all were enetered, albeit with a different error message.

-** A function called get_n_type() was then called, whose sole purpose was to take n and discover if n was odd or even, and if even,
doubly or singly so, and then return the result.

-** A function called get_n_center() was then called, which, depending on the result of get_n_type(), would simply return a value
necessary to perform the Siamese Method.

A list was then initialized, containing all numbers from 1 to n squared.

-** A function called get_goal() was then called, whose purpose was to discover the magic number to which all rows, columns, and
diagonals must sum, with the expression goal = (n * (squared + 1)) // 2. It would then print several statements about the
square-to-be, including the magic number.

An initial square of size n by n was then created filled with zeros with np.zeros, which would be useful for the Siamese Method.

Next, based on the n_type, the function containing the appropriate algorithm for creatiing the magic square was called.

-** Since these algorithms will output the exact same square each time, a function called rotate() was next called, which
turned or flipped the square in a random fashion, to add a bit of mystery but mostly for aesthetic purposes.

-** The function check_sums() was then called, whose purpose was to take the square and calculate the sums of each of its
rows, columns, and diagonals. Regardless of the outcome, it will then print those numbers, which was useful for debugging.
If all sums do not equal the magic number, the funcction will return False, and the incorrect square will be printed as a simple
NumPy array together with a discouraging message. If all sums do in fact equal the magic number, the function will return True,
and the square will be returned.

If n was less then 31, it will be printed inside a tabulate heavy_grid, so that each number gets its own cell, again for aesthetic
purposes. If n was more than 31, then when tabulate is used it gets outputted to terminal in a really weird way because of how big
the square is, so it instead gets outputted as a simple NumPy array. However due to the size of the square at such high n, only the
corners of the array will outputted. If one looks at the outputted sums, however, one can tell that this is still in fact a magic
square.

Either way, you get a congratulatory message.


Additionally, a test_project.py file was written containing several test on some of the custom function if the program,
namely checking that the functions get_goal, get_n_center, get_n_type, and check_sums are all working as expected.

A requirements.txt file was also created to record the names of the pip-installable libraries used in this project, namely
NumPy and tabulate, as this was apparently required.