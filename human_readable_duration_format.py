def format_duration(seconds) -> str:
    # [y, d, h, m, s]
    if seconds <= 0:
        return "now"
    else:
        y, d, h, m = 0, 0, 0, 0
        # year(s)
        if seconds//31536000 >= 1:
            y = seconds//31536000
            seconds = seconds % 31536000
        # day(s)
        if seconds//86400 >= 1:
            d = seconds // 86400
            seconds = seconds % 86400
        # hour(s)
        if seconds//3600 >= 1:
            h = seconds // 3600
            seconds = seconds % 3600
        # minute(s)
        if seconds//60 >= 1:
            m = seconds // 60
            seconds = seconds % 60
        comma_str = ", "
        and_str = " and "
        duration = [y, d, h, m, seconds]
        duration_str = [y.__str__() + (" years" if y>1 else " year"),
                        d.__str__() + (" days" if d>1 else " day"),
                        h.__str__() + (" hours" if h>1 else " hour"),
                        m.__str__() + (" minutes" if m>1 else " minute"),
                        seconds.__str__() + (" seconds" if seconds>1 else " second")]
        nn = 5 - duration.count(0)
        returning = ""
        for i in range(5):
            if duration[i] > 0:
                if nn == 1:
                    returning = returning + duration_str[i]
                elif nn > 2:
                    returning = returning + duration_str[i] + comma_str
                elif nn == 2:
                    returning = returning + duration_str[i] + and_str
                nn -= 1
        return returning


print(format_duration(10))
