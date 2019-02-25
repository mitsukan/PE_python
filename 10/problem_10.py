
class Prob10(object):

    def is_prime(self, num):
        div_count = 0
        count = num
        # Initial check for numbers 0 and 1
        if num == 0 or num == 1:
            return False
        else:
            # Looping backwards
            while count > 0:
                # if number is divisible by current number
                if num % count == 0:
                    # Add to divisible count
                    div_count += 1
                count -= 1
        # If divider count is more than 2, return false
        if div_count > 2:
            return False
        # Else if number can only be divisble by itself and 1
        elif div_count == 2:
            return True

