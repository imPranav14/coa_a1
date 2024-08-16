#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

void matrixMultiplyInteger(int N) {
    vector<vector<int>> A(N, vector<int>(N, 1));
    vector<vector<int>> B(N, vector<int>(N, 1));
    vector<vector<int>> C(N, vector<int>(N, 0));

    // Matrix multiplication logic (meat portion)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int sizes[] = {64, 128, 256, 512, 1024};

    for (int N : sizes) {
        timespec total_start, total_end, meat_start, meat_end;

        // Start timing the entire program execution
        clock_gettime(CLOCK_MONOTONIC, &total_start);

        // Start timing just before the matrix multiplication function call
        clock_gettime(CLOCK_MONOTONIC, &meat_start);

        matrixMultiplyInteger(N);

        // End timing just after the matrix multiplication function call
        clock_gettime(CLOCK_MONOTONIC, &meat_end);

        // End timing the entire program execution
        clock_gettime(CLOCK_MONOTONIC, &total_end);

        double meat_time = meat_end.tv_sec - meat_start.tv_sec + (meat_end.tv_nsec - meat_start.tv_nsec) / 1e9;
        double total_time = total_end.tv_sec - total_start.tv_sec + (total_end.tv_nsec - total_start.tv_nsec) / 1e9;
        double meat_percentage = (meat_time / total_time) * 100;

        cout << "Total time for Integer matrix multiplication of size " << N << "x" << N << ": " << total_time << " seconds" << endl;
        cout << "Meat time: " << meat_time << " seconds" << endl;
        cout << "Percentage of meat time: " << meat_percentage << "%" << endl;
        cout << "-----------------------------------" << endl;
    }

    return 0;
}
