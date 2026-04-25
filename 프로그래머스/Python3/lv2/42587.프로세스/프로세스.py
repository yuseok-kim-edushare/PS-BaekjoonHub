def solution(jobs, location):
    #jobs: queue of job's priority
    #location: interested job's location
    count = 0
    while location != -1:
        if location == 0:
            if jobs[0] == max(jobs):
                count += 1
                location = -1
                #now interested job done
            else:
                jobs.append(jobs.pop(0))
                #queue pop and queue push
                location = len(jobs) - 1
                #now our interested job in top
        elif jobs[0] == max(jobs):
            jobs.pop(0)
            count += 1
            location -= 1
            #trace our interested job is where
        else:
            jobs.append(jobs.pop(0))
            location -= 1
    
    return count