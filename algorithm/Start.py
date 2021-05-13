from algorithm import ant_TSP, DP_TSP, generate_coordinate


def Average(lst):
    return sum(lst) / len(lst)



def _relative_error(int_1, int_2):
    return (int_1 - int_2) / abs(int_2)


result_DP_runtime = []
result_DP_optimal_cost = []
result_ant_Runtime = []
result_ant_BestScore = []
result_relative_error = []


n_point = int(input("How many Point You Want?(From 4): "))
# generate = generate_coordinate


for i in range(20, (n_point + 1)):
    generate = generate_coordinate
    input_size = i  # How many point we have
    temp_result_DP_runtime = []
    temp_result_DP_optimal_cost = []
    temp_result_ant_Runtime = []
    temp_result_ant_BestScore = []
    for j in range(5):
        coordinates, distance_array = generate.generate_random_input(input_size)

        #   DP_TSP
        # if i == n_point:
        #     plot = True
        # else:
        #     plot = False

        DP_runtime, DP_optimal_cost, DP_optimal_path = DP_TSP.INPUT_DP_TSP(coordinates, distance_array, index_plot=False)

        #   ANT_TSP
        ant_TSP_model = ant_TSP
        ant_BestScore, ant_Runtime = ant_TSP_model.INPUT_Ant_TSP(distance_array)

        #   Store Result：
        temp_result_ant_BestScore.append(ant_BestScore)
        temp_result_ant_Runtime.append(ant_Runtime)
        temp_result_DP_optimal_cost.append(DP_optimal_cost)
        temp_result_DP_runtime.append(DP_runtime)

    result_ant_BestScore.append(sum(temp_result_ant_BestScore))
    result_ant_Runtime.append(Average(temp_result_ant_Runtime))
    result_DP_optimal_cost.append(sum(temp_result_DP_optimal_cost))
    result_DP_runtime.append(Average(temp_result_DP_runtime))
    result_relative_error.append(
        _relative_error(
            sum(temp_result_ant_BestScore), sum(temp_result_DP_optimal_cost)
        )
    )

    #   Saving Result(Real Time)
    fn = 'output_v3.txt'    # File name

    with open(fn, 'w')as file_Obj:
        file_Obj.write('result_ant_BestScore=' + str(result_ant_BestScore) + '\n')
        file_Obj.write('result_ant_Runtime=' + str(result_ant_Runtime) + '\n')
        file_Obj.write('result_DP_optimal_cost=' + str(result_DP_optimal_cost) + '\n')
        file_Obj.write('result_DP_runtime=' + str(result_DP_runtime) + '\n')
        file_Obj.write('result_relative_error=' + str(result_relative_error) + '\n')



