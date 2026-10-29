import random

num_customers = 100
total_wait_time = 0
total_service_time = 0
total_interarrival_time = 0
total_time_in_system = 0
total_idle_time = 0
customers_who_wait = 0

prev_arrival_time = 0
prev_service_end_time = 0

results = []

print("Cust | Interarr | Arrival | Service | Srv Begin | Wait | Srv End | In System | Idle")
print("-" * 85)

for i in range(1, num_customers + 1):
    interarrival = random.randint(1, 8)
    
    arrival_time = prev_arrival_time + interarrival
    
    r = random.random()
    if r < 0.10:
        service_time = 1
    elif r < 0.30:
        service_time = 2
    elif r < 0.60:
        service_time = 3
    elif r < 0.85:
        service_time = 4
    elif r < 0.95:
        service_time = 5
    else:
        service_time = 6
        
    if arrival_time > prev_service_end_time:
        service_begin = arrival_time
        idle_time = arrival_time - prev_service_end_time
    else:
        service_begin = prev_service_end_time
        idle_time = 0
        
    wait_time = service_begin - arrival_time
    
    service_end = service_begin + service_time
    
    time_in_system = wait_time + service_time
    
    total_wait_time += wait_time
    total_service_time += service_time
    total_interarrival_time += interarrival
    total_time_in_system += time_in_system
    total_idle_time += idle_time
    
    if wait_time > 0:
        customers_who_wait += 1
        
    prev_arrival_time = arrival_time
    prev_service_end_time = service_end
    
    print(f"{i:4} | {interarrival:8} | {arrival_time:7} | {service_time:7} | {service_begin:9} | {wait_time:4} | {service_end:7} | {time_in_system:9} | {idle_time:4}")

print("\n--- Final Results (Measures of Performance) ---")
avg_wait = total_wait_time / num_customers
print(f"1. Average Waiting Time: {avg_wait:.2f}")

prob_wait = customers_who_wait / num_customers
print(f"2. Probability (wait): {prob_wait:.2f}")

prob_idle = total_idle_time / prev_service_end_time
print(f"3. Probability idle server: {prob_idle:.2f}")

avg_service = total_service_time / num_customers
print(f"4. Average service time: {avg_service:.2f}")

avg_interarrival = total_interarrival_time / num_customers
print(f"5. Average time between arrivals: {avg_interarrival:.2f}")

if customers_who_wait > 0:
    avg_wait_those_who_wait = total_wait_time / customers_who_wait
else:
    avg_wait_those_who_wait = 0
print(f"6. Average waiting time of those who wait: {avg_wait_those_who_wait:.2f}")

avg_time_in_system = total_time_in_system / num_customers
print(f"7. Average time a customer spends in the system: {avg_time_in_system:.2f}")