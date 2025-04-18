# %% [markdown]
# # Imported Libraries

# %%
import random

# %% [markdown]
# # Random List

# %%
def random_list(n):
  """
  Returns a list of n random integers between 1 and n.
  """
  return [random.randint(1, n) for _ in range(n)]

# %% [markdown]
# # Sorted List

# %%
def sorted_list(n):
  """
  Returns a list of n integers in ascending order.
  """
  return list(range(1, n+1))

# %% [markdown]
# # Reversed List

# %%
def reversed_list(n):
  """
  Returns a list of n integers in descending order.
  """
  return list(range(n, 0, -1))


