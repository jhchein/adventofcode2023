import re

def process_combination_dp(springs, target):
    springs = springs.strip(".").replace('.', '0').replace('#', '1') + '0'
    springs = re.sub(r'0+', '0', springs)
    target = [int(x) for x in target.split(',')]
    memo = {}

    def dp_helper(index, target_index, consecutive_ones):
        if target_index >= len(target):
            return 0
        if index >= len(springs):
            return 0
        
        current_target = target[target_index]
        current_char = springs[index]

        ways = 0
        # If we have too many consecutive ones, we can't continue
        if consecutive_ones > current_target:
            return 0 
        # If we reach the end of the string and reached the target, or if we reach the target and there are only zeros and /or "?" left, we have a valid combination
        if (index == len(springs) and target_index == len(target) and consecutive_ones == current_target) or \
           (target_index == len(target) - 1 and consecutive_ones >= current_target and re.fullmatch(r'[0\?]+', springs[index:])):
            return 1
        
        # If we have a memorized value, return it
        if (index, target_index, consecutive_ones) in memo:
            return memo[(index, target_index, consecutive_ones)]
        
        # If we encounter a zero, we continue with consecutive ones set to 0
        if current_char == '0':
            # If we have too few consecutive ones and encounter a zero, we can't continue
            if 1 <= consecutive_ones < current_target:
                return 0
            # If we reach the target, go to the next target
            elif consecutive_ones == current_target:
                ways += dp_helper(index + 1, target_index + 1, 0)
            else:
                ways += dp_helper(index + 1, target_index, 0)
        
        # If we encounter a one, we continue with consecutive ones set to 1
        elif current_char == '1':
            if consecutive_ones >= current_target:
                return 0
            else:
                ways += dp_helper(index + 1, target_index, consecutive_ones + 1)

        # If we encounter a question mark, we continue with consecutive ones set to 0 and 1
        elif current_char == '?':
            # If we reach the target, we can't choose 1
            if consecutive_ones == current_target:
                if target_index == len(target) - 1:
                    if re.fullmatch(r'[0\?]+', springs[index:]):
                        return 1
                    else:
                        return 0
                ways += dp_helper(index + 1, target_index+1, 0)
            # if we're in the middle of a consecutive ones sequence, we can't choose 0
            elif current_target > consecutive_ones > 0:
                ways += dp_helper(index + 1, target_index, consecutive_ones + 1)
            else:
                # Choose 1
                ways += dp_helper(index + 1, target_index, consecutive_ones + 1)
                # Choose 0
                ways += dp_helper(index + 1, target_index, 0)
                
        
        memo[(index, target_index, consecutive_ones)] = ways
        return ways
    
    return dp_helper(0, 0, 0)


# Example usage
if __name__ == "__main__":
    print(f'{process_combination_dp("???.###", "1,1,3")}, should be 1')
    print(f'{process_combination_dp(".??..??...?##.", "1,1,3")}, should be 4')
    print(f'{process_combination_dp("????.######..#####.", "1,6,5")}, should be 4')
    print(f'{process_combination_dp("????.#...#...", "4,1,1")}, should be 1')
    print(f'{process_combination_dp("?#?#?#?#?#?#?#?", "1,3,1,6")}, should be 1')
    print(f'{process_combination_dp("?###????????", "3,2,1")}, should be 10')
