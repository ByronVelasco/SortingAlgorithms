# %% [markdown]
# ## Bubble Sort Algorithm

# %%
def BubbleSort(A):
  """
  Sorts a list using the Bubble Sort algorithm.
  """
  n = len(A)
  for i in range(0, n-1):
    for j in range(n-1, i, -1):
      if A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j]


