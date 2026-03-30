class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]   # store pages
        self.current = 0            # pointer to current page

    def visit(self, url: str) -> None:
        # remove forward history
        self.history = self.history[:self.current + 1]
        
        # add new page
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        # move left but not less than 0
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # move right but not beyond list
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]