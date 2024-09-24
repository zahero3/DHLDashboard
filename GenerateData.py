import pandas as pd
import numpy as np
import random

def generateData(rows,year):
    
    # Set random seed for reproducibility
    np.random.seed(1)

    num_records = rows
    yr = year
    
    # Random shipment dates
    dates = pd.date_range(start= str(yr)+'-01-01', periods=365, freq='D')
    shipment_dates = np.random.choice(dates, num_records)

    # Carrier options
    carriers = ['Carrier A', 'Carrier B', 'Carrier C', 'Carrier D']
    carrier_weights = [0.25,0.3,0.1,0.35]
    carriers_sample = np.random.choice(carriers, num_records, p=carrier_weights)
    
    # Warehouse options
    warehouses = ['Warehouse 1', 'Warehouse 2', 'Warehouse 3', 'Warehouse 4']
    wareh_weights = [0.3,0.04,0.6,0.06]
    warhse_sample = np.random.choice(warehouses, num_records, p=wareh_weights)
    
    # Regions with uneven distribution
    regions = ['Europe', 'North America', 'Asia', 'South America', 'Africa', 'Oceania']
    region_weights = [0.35, 0.25, 0.2, 0.1, 0.05, 0.05]
    regions_sample = np.random.choice(regions, num_records, p=region_weights)

    # Gender distribution (60% male, 40% female)
    genders = np.random.choice(['Male', 'Female'], num_records, p=[0.6, 0.4])

    # Random numeric fields
    shipment_cost = np.round(np.random.uniform(50, 500, num_records), 2)
    order_accuracy = np.random.choice(['Yes', 'No'], num_records, p=[0.87, 0.13]) #change % as per need 
    delivery_status = np.random.choice(['On-Time', 'Delayed'], num_records, p=[0.94, 0.06]) #change % as per need
    warehouse_utilization = np.round(np.random.uniform(85, 95, num_records), 2) #change % as per need
    lead_time = np.round(np.random.uniform(1, 15, num_records), 1)
    customer_satisfaction = np.random.randint(1, 11, num_records)
    returns = np.random.choice(['Yes', 'No'], num_records, p=[0.32, 0.68]) #change % as per need
    product_type = np.random.choice(['Automotive Parts','Pharmaceuticals',
                                     'Consumer Electronics'], num_records, p=[0.23,0.44,0.33]) #change % as per need

    # Create DataFrame
    df = pd.DataFrame({
        'Shipment_ID': range(1, num_records+1),
        'Shipment_Date': shipment_dates,
        'Carrier': carriers_sample,
        'Warehouse': warhse_sample,
        'Region': regions_sample,
        'Shipment_Cost': shipment_cost,
        'Delivery_Status': delivery_status,
        'Order_Accuracy': order_accuracy,
        'Warehouse_Utilization': warehouse_utilization,
        'Lead_Time': lead_time,
        'Gender': genders,
        'Customer_Satisfaction': customer_satisfaction,
        'Returns': returns,
        'Product_type': product_type
    })

    # Save as CSV
    df.to_csv('supply_chain_data'+str(yr)+'.csv', index=False)
    print('Generated!')

#Call the above function
generateData(124987,2024)
