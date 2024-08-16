import matplotlib.pyplot as plt

# Data for C++ integer operations
matrix_sizes = [64, 128, 256, 512, 1024]
cpp_system_times = [0.349, 0.420, 0.534, 1.772, 7.173]

# Data for Python integer operations
python_sizes = [64, 128, 256, 512, 1024]
python_system_times = [0.288, 0.760, 4.510, 37.738, 309.71]

# Create a line plot
plt.figure(figsize=(10, 6))

# Plot C++ data
plt.plot(matrix_sizes, cpp_system_times, marker='o', linestyle='-', color='b', label='C++ Integer Operations')

# Plot Python data
plt.plot(python_sizes, python_system_times, marker='o', linestyle='-', color='r', label='Python Integer Operations')

# Adding title and labels
plt.title('System Time vs Matrix Size for Integer Operations')
plt.xlabel('Matrix Size (NxN)')
plt.ylabel('System Time (seconds)')

# Adding a legend
plt.legend()

# Adding grid
plt.grid(True)

# Show the plot
plt.show()



# Data for C++ float operations
cpp_float_sizes = [64, 128, 256, 512, 1024]
cpp_float_system_times = [0.348, 0.980, 1.266, 1.201, 7.326]

# Data for Python float operations
python_float_sizes = [64, 128, 256, 512, 1024]
python_float_system_times = [0.236, 0.795, 4.914, 39.461, 738.64]

# Create a line plot
plt.figure(figsize=(10, 6))

# Plot C++ float operations
plt.plot(cpp_float_sizes, cpp_float_system_times, marker='o', linestyle='-', color='b', label='C++ Float Operations')

# Plot Python float operations
plt.plot(python_float_sizes, python_float_system_times, marker='o', linestyle='-', color='g', label='Python Float Operations')

# Adding title and labels
plt.title('System Time vs Matrix Size for Float Operations')
plt.xlabel('Matrix Size (NxN)')
plt.ylabel('System Time (seconds)')

# Adding a legend
plt.legend()

# Adding grid
plt.grid(True)

# Show the plot
plt.show()



# Data for C++ integer operations
cpp_sizes = [64, 128, 256, 512, 1024]
cpp_meat_times = [0.005388, 0.032153, 0.136549, 0.752938, 5.89173]

# Data for Python integer operations
python_sizes = [64, 128, 256, 512, 1024]
python_meat_times = [0.107969, 0.635660, 4.407973, 37.624068, 309.580205]

# Create a line plot
plt.figure(figsize=(10, 6))

# Plot C++ meat times
plt.plot(cpp_sizes, cpp_meat_times, marker='o', linestyle='-', color='m', label='C++ Integer Operations')

# Plot Python meat times
plt.plot(python_sizes, python_meat_times, marker='o', linestyle='-', color='b', label='Python Integer Operations')

# Adding title and labels
plt.title('Meat Time vs Matrix Size for Integer Operations')
plt.xlabel('Matrix Size (NxN)')
plt.ylabel('Meat Time (seconds)')

# Adding a legend
plt.legend()

# Adding grid
plt.grid(True)

# Show the plot
plt.show()



# Data for C++ float operations
cpp_float_sizes = [64, 128, 256, 512, 1024]
cpp_float_meat_times = [0.005706, 0.026751, 0.132606, 0.785699, 6.91531]

# Data for Python float operations
python_float_sizes = [64, 128, 256, 512, 1024]
python_float_meat_times = [0.110574, 0.670357, 4.802179, 37.624068, 738.520173]

# Create a line plot
plt.figure(figsize=(10, 6))

# Plot C++ float operations
plt.plot(cpp_float_sizes, cpp_float_meat_times, marker='o', linestyle='-', color='c', label='C++ Float Operations')

# Plot Python float operations
plt.plot(python_float_sizes, python_float_meat_times, marker='o', linestyle='-', color='r', label='Python Float Operations')

# Adding title and labels
plt.title('Meat Time vs Matrix Size for Float Operations')
plt.xlabel('Matrix Size (NxN)')
plt.ylabel('Meat Time (seconds)')

# Adding a legend
plt.legend()

# Adding grid
plt.grid(True)

# Show the plot
plt.show()
