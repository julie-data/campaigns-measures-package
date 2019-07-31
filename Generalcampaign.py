from datetime import date
import datetime

class Campaign:
    
    def __init__(self, campaign_name, start_date, end_date, eligible_customers, control_proportion):
        
        """ Generic campaign class to calculate 
        performance metrics on the campaign.
        
        Attributes
            name (string) representing the campaign name
            start_date (string YYYY-MM-DD) representing the first day of the campaign
            end_date (string YYYY-MM-DD) representing the last day of the campaign
            eligible_customers (float) representing the number of customers eligible
            control_proportion (flot) representing the proportion of customers in the control group
            length (float) the campaign length in days
            treatment_size (float) the number of eligible customers in the treatment group
            control_size (float) the number of eligible customers in the control group
            """
        
        self.name = campaign_name
        self.start = start_date
        self.end = end_date
        self.eligible_customers = eligible_customers
        self.control_proportion = control_proportion
        self.length = 0
        self.treatment_size = 0
        self.control_size = 0
        
    def calculate_length(self):
        
        """ Function to calculate the length of the campaign
        in days.
        
        Args:
            None
            
        Returns:
            None
        """
        
        format_str = '%Y-%m-%d'
        delta = datetime.strptime(self.end, format_str) - datetime.strptime(self.start, format_str)
        
        self.length = delta.days
        
    def calculate_group_sizes(self):
        
        """Function to calculate the number of eligible customers
        in the treatment and control groups.
        
        Args:
            None
            
        Returns:
            None
        """
        
        self.treatment_size = self.eligible_customers * (1 - self.control_proportion)
        self.control_size = self.eligible_customers * self.control_proportion