from .Generalcampaign import Campaign

class Email(Campaign):
    """Email campaign class for calculating measures
    about the campaign success.
    
     Attributes
        name (string) representing the campaign name
        start_date (string YYYY-MM-DD) representing the first day of the campaign
        end_date (string YYYY-MM-DD) representing the last day of the campaign
        eligible_customers (float) representing the number of customers eligible
        control_proportion (flot) representing the proportion of customers in the control group
        number_opened (float) the number of customers who have opened the email
        number_opted_out (float) the number of customers who have opted out from the email
        number_bought (float) the number of customers who have purchased the unit advertised
     """
    
    def __init__(self, name, start, end, eligible_customers, control_proportion
                 , number_opened, number_opted_out, number_bought):
        
        Campaign.__init__(self, name, start, end, eligible_customers, control_proportion)
        self.opened = number_opened
        self.opted_out = number_opted_out
        self.bought = number_bought
        
    def calculate_adjusted_population(self, opt_out_rate):
        
        """Function to calculate the adjusted eligible population, depending
        on the usual opt-out rate.
        
        Args:
            opt_out_rate (float) representing the usual opt out rate
            
        Returns:
            adjusted_treatment (float) the adjusted number of customers in the treatment group
            adjusted_control (float) the adjusted number of customers in the control group
        """
    
        adjusted_population = self.eligible_customers * (1 - opt_out_rate)
        adjusted_treatment = self.calculate_treatment_size() * (1 - opt_out_rate)
        adjusted_control = self.calculate_control_size() * (1 - opt_out_rate)
        
        return adjusted_treatment, adjusted_control, adjusted_population