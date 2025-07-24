

class OverlappingWindowSplit:
    def __init__(self, M, window_size=100, step_size=1, n_windows=10):
        self.M = M
        self.n_rows = len(M)
        self.n_cols = len(M[0])
        self.window_size = window_size
        self.step_size = step_size
        self.n_windows = n_windows

    def __iter__(self):
        M = self.M
        n_rows = self.n_rows
        n_cols = self.n_cols
        window_size = self.window_size
        step_size = self.step_size
        n_windows = self.n_windows
        
        # Selecting n_windows of windows from the end of the matrix
        # Each window ends step_size 'rows' appart 
        for i in range(0, n_windows):
            start = n_rows - (window_size + (n_windows - i) * step_size)
            end = start + window_size
            yield M[start:end]
