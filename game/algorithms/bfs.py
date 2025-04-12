from collections import deque
from game.world_generator import World

DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def bfs(row, col, world: World) -> list[tuple[int, int]] | None:
    queue = deque()
    start = (row, col)
    path = [start]
    queue.append((start, path))
    visited = set()
    end = None
    for r in range(world.ROWS):
        for c in range(world.COLS):
            if world.MAP[r][c] == "E":
                end = (r, c)
    
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        
        for dr, dc in DIRECTIONS:    
            nr, nc = r + dr, c + dc
            if 0 <= nr < world.ROWS and 0 <= nc < world.COLS \
                and world.MAP[nr][nc] in ("0", "S", "E") and (nr, nc) not in visited:
                queue.append(((nr, nc), path + [(nr, nc)]))
                visited.add((nr, nc))
        
    return None
            



