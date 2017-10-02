def rotate(state, pipe_numbers):
    pipe_count = len(state)
    working_configs = []

    for i in range(pipe_count):
        if 0 not in [state[i] for i in pipe_numbers]:
            working_configs.append(i)
        state.insert(0, state.pop())

    return working_configs
