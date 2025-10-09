// Last updated: 10/8/2025, 9:48:09 PM
public class Solution {
public int[] GetAverages(int[] nums, int k)
{
    if (k == 0)
    {
        return nums;
    }
    int windowSize = 2 * k + 1;
    int n = nums.Length;
    int[] averages = Enumerable.Repeat(-1, n).ToArray();


    if (windowSize > n)
    {
        return averages;
    }
    long[] prefix = new long[n + 1];
    for (int i = 0; i < n; i++)
    {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    for (int i = k; i < (n - k); ++i)
    {
        int leftBound = i - k, rightBound = i + k;
        long subArraySum = prefix[rightBound + 1] - prefix[leftBound];
        int average = Convert.ToInt32(subArraySum / windowSize);
        averages[i] = average;
    }

        return averages;


    }
}