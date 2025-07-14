import safemath

def Income_Statement():
    def Revenue():#2 models
        def Gross_sales_model():
            return safemath.Decimal(0)
        def discounts_model():
            return safemath.Decimal(0)
        Gross_sales = Gross_sales_model()
        Less_sales_returns_and_allowances = discounts_model()
        Net_Sales = safemath.add1(Gross_sales, Less_sales_returns_and_allowances)
        return {
            "Gross_sales": Gross_sales,
            "Less_sales_returns_and_allowances": Less_sales_returns_and_allowances,
            "Net_Sales":  Net_Sales
            }
        
    def COGS(Net_Sales):#5 models
        def Beginning_inventory_model():
            return safemath.Decimal(0)
        def Goods_purchased_model():
            return safemath.Decimal(0)
        def Goods_manufactured_Raw_materials_model():
            return safemath.Decimal(0)
        def Goods_manufactured_Direct_labor_model():
            return safemath.Decimal(0)
        def ending_inventory_model():
            return safemath.Decimal(0)
        Beginning_inventory = Beginning_inventory_model()
        Goods_purchased= Goods_purchased_model()
        Goods_manufactured_Raw_materials= Goods_manufactured_Raw_materials_model()
        Goods_manufactured_Direct_labor= Goods_manufactured_Direct_labor_model()
        Total_Goods_Available = safemath.add2([Beginning_inventory, Goods_purchased, Goods_manufactured_Raw_materials,  Goods_manufactured_Direct_labor])
        Less_ending_inventory = ending_inventory_model()
        Cost_of_Goods_Sold = safemath.add1(Total_Goods_Available, Less_ending_inventory)
        Gross_Profit = safemath.add1(Net_Sales, Cost_of_Goods_Sold)
        return {
            "Beginning_inventoy": Beginning_inventory,
            "Goods_purchased": Goods_purchased,
            "Goods_manufactured_Raw materials": Goods_manufactured_Raw_materials,
            "Goods_manufactured_Direct_labor": Goods_manufactured_Direct_labor,
            "Total_Goods_Available": Total_Goods_Available,
            "Less_ending_inventory": Less_ending_inventory,
            "Cost_of_Goods_Sold": Cost_of_Goods_Sold,
            "Gross_Profit": Gross_Profit
            }

    def Expenses(Gross_Profit):#20 models
        def Advertising_model():
            return safemath.Decimal(0)
        def Bad_debt_model():
            return safemath.Decimal(0)
        def Commissions_model():
            return safemath.Decimal(0)
        def Employee_benefits_model():
            return safemath.Decimal(0)
        def Furniture_and_equipment_model():
            return safemath.Decimal(0)
        def Insurance_model():
            return safemath.Decimal(0)
        def Maintenance_and_repairs_model():
            return safemath.Decimal(0)
        def Office_supplies_model():
            return safemath.Decimal(0)
        def Payroll_taxes_model():
            return safemath.Decimal(0)
        def Rent_model():
            return safemath.Decimal(0)
        def Research_and_development_model():
            return safemath.Decimal(0)
        def Salaries_and_wages_model():
            return safemath.Decimal(0)
        def Software_model():
            return safemath.Decimal(0)
        def Travel_model():
            return safemath.Decimal(0)
        def Utilities_model():
            return safemath.Decimal(0)
        def Web_hosting_and_domains_model():
            return safemath.Decimal(0)
        def Other_model():
            return safemath.Decimal(0)
        def Non_operating_revenues_expenses_gains_losses_model():
            return safemath.Decimal(0)
        def interest_expense_model():
            return safemath.Decimal(0)
        def income_tax_expense_model():
            return safemath.Decimal(0)
        Advertising = Advertising_model()
        Bad_debt = Bad_debt_model()
        Commissions = Commissions_model()
        Depreciation = Depreciation_model()
        Employee_benefits = Employee_benefits()
        Furniture_and_equipment = Furniture_and_equipment_model()
        Insurance = Insurance_model()
        Maintenance_and_repairs = Maintenance_and_repairs_model()
        Office_supplies = Office_supplies_model()
        Payroll_taxes = Payroll_taxes_model()
        Rent = Rent_model()
        Research_and_development = Research_and_development_model()
        Salaries_and_wages = Salaries_and_wages_model()
        Software = Software_model()
        Travel = Travel_model()
        Utilities = Utilities_model()
        Web_hosting_and_domains = Web_hosting_and_domains_model()
        Other = Other_model()
        Total_Operating_Expenses = safemath.add2([Advertising, Bad_debt, Commissions, Depreciation, Employee_benefits, Furniture_and_equipment, Insurance, Maintenance_and_repairs, Office_supplies, Payroll_taxes, Rent, Research_and_development, Salaries_and_wages, Software, Travel, Utilities, Web_hosting_and_domains, Other])
        Operating_Income = safemath.add1(Gross_Profit, Total_Operating_Expenses)
        Non_operating_revenues_expenses_gains_losses = Non_operating_revenues_expenses_gains_losses_model()
        Less_interest_expense = interest_expense_model()
        Income_Before_Taxes = safemath.add2([Operating_Income, Non_operating_revenues_expenses_gains_losses, Less_interest_expense])
        Less_income_tax_expense = income_tax_expense_model()
        Income_From_Continuing_Operations = safemath.add1(Income_Before_Taxes, Less_income_tax_expense)
        return {
            "Advertising": Advertising,
            "Bad_debt": Bad_debt,
            "Commissions": Commissions,
            "Depreciation": Depreciation,
            "Employee_benefits": Employee_benefits,
            "Furniture_and_equipment": Furniture_and_equipment,
            "Insurance": Insurance,
            "Maintenance_and_repairs": Maintenance_and_repairs,
            "Office_supplies": Office_supplies,
            "Payroll_taxes": Payroll_taxes,
            "Rent": Rent,
            "Research_and_development": Research_and_development,
            "Salaries_and_wages": Salaries_and_wages,
            "Software": Software,
            "Travel": Travel,
            "Utilities": Utilities,
            "Web_hosting_and_domains": Web_hosting_and_domains,
            "Other": Other,
            "Total_Operating_Expenses": Total_Operating_Expenses,
            "Operating_Income": Operating_Income,
            "Non_operating_revenues_expenses_gains_losses": Non_operating_revenues_expenses_gains_losses,
            "Less_interest_expense": Less_interest_expense,
            "Income_Before_Taxes": Income_Before_Taxes,
            "Less_income_tax_expense": Less_income_tax_expense,
            "Income_From_Continuing_Operations": Income_From_Continuing_Operations
            }

    def Below_the_line_items(Income_From_Continuing_Operations):#3 models
        def Income_from_discontinued_operations_model():
            return safemath.Decimal(0)
        def Extraordinary_items_model():
            return safemath.Decimal(0)
        def Cumulative_effect_of_accounting_changes_model():
            return safemath.Decimal(0)
        Income_from_discontinued_operations = Income_from_discontinued_operations_model()
        Extraordinary_items = Extraordinary_items_model()
        Cumulative_effect_of_accounting_changes = Cumulative_effect_of_accounting_changes_model()
        Net_Income = safemath.add2([Income_From_Continuing_Operations, Income_from_discontinued_operations, Extraordinary_items, Cumulative_effect_of_accounting_changes])
        return {
            "Income_from_discontinued_operations": Income_from_discontinued_operations,
            "Extraordinary_items": Extraordinary_items,
            "Cumulative_effect_of_accounting_changes": Cumulative_effect_of_accounting_changes,
            "Net_Income": Net_Income
            }

    revenue = Revenue() 
    cogs = COGS(revenue['Net_Sales'])
    expenses = Expenses(cogs['Gross_Profit'])
    btli = Below_the_line_items(expenses['Income_From_Continuing_Operations'])
    return {
        "Revenue": revenue,
        "Cost_of_Goods_Sold": cogs,
        "Expenses": expenses,
        "Below_the_line_items": btli
        }

print(Income_Statement())