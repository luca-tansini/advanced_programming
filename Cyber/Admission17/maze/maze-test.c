#include <stdio.h>
#include "maze.h"

char maze48x13[] = "+ ---------------------------------------------+"
                   "| |  |         |        |     |                |"
                   "| | -+-- +---+ +-- +--- +-- +-+ +--- +-------- |"
                   "| |      |   | |   |    |   | | |    |         |"
                   "| +-- ---+ | | | --+-+  | |     +--- +--+ -----+"
                   "|          | | |   | +--+ +-----+       |      |"
                   "| +----+---+ | +-- | |  |       +- --+--+-+--- +"
                   "| |    |     |     | ++ ++ -+-+ |    |    |    |"
                   "| +-- -+- ---+- ---+  |  |  | +-+--- +--+ + -+ |"
                   "|      |    |      | +++ |    |      |  |    | |"
                   "+---- -+--- | ---+ + | | +--- | --+--+ -+ +--+ +"
                   "|           |    |            |   |       |    |"
                   "+-----------+----+----------------+-------+--- +";

char maze11x6[] = "+ ------+-+"
                  "| |     | |"
                  "| | +-+ | |"
                  "| | +-+ | |"
                  "|       | |"
                  "+------ + +";

char maze5x3[] = "     "
                 "     "
                 "     ";

static void print_maze(const char* maze, unsigned w, unsigned h) {
    unsigned i;
    for (i=0; i<h*w; i += w)
        fwrite(maze+i, sizeof(char), w, stdout),
        puts("");
}

static void check_solution(char* maze, char* path,
                           unsigned w, unsigned h,
                           const char* msg, int test_no) {
    char* map = "0123";
    int i = 0, x = 1, y = 0;

    unsigned len = solve_maze(maze, w, h, path);

    printf("\ntest #%d >> returned path length = %d [correct %s]\n",
            test_no, len, msg);

    if (len > 0) {
        for (;; ++i) {
            if (x < 0 || x >= w ||
                y < 0 || y >= h || maze[y*w+x] != ' ') goto err;
            if (i == len) break;
            maze[y*w+x] = map[(int)path[i]];
            x += path[i] == 1 ? 1 : path[i] == 3 ? -1 : 0;
            y += path[i] == 0 ? 1 : path[i] == 2 ? -1 : 0;
        }
        if (x != w-2 || y != h-1) goto err;
        maze[y*w+x] = 'X';
    }
    print_maze(maze, w, h);
    return;
err:
    fprintf(stderr, "[error] wrong solution...\n");
    print_maze(maze, w, h);
}

int main() {

    // test #1
    char path48x13[sizeof(maze48x13)];
    check_solution(maze48x13, path48x13, 48, 13, "> 0", 1);

    // test #2
    char path11x6[sizeof(maze11x6)];
    check_solution(maze11x6, path11x6, 11, 6, "= 0", 2);

    // test #3
    char path5x3[sizeof(maze5x3)];
    check_solution(maze5x3, path5x3, 5, 3, "> 0", 3);

    return 0;
}
