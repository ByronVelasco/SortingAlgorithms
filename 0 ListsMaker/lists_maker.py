# %% [markdown]
# # Imported Libraries

# %%
import random

# %% [markdown]
# # Random List

# %%
def random_list(n):
  return [random.randint(1, n) for _ in range(n)]

# %% [markdown]
# # Sorted List

# %%
def sorted_list(n):
  return list(range(1, n+1))

# %% [markdown]
# # Reversed List

# %%
def reversed_list(n):
  return list(range(n, 0, -1))


