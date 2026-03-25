
class SpitWise:
    def solution(self):
        payment_summary={
            "hari":1200,
            "vipin":1400,
            "jhon":1000,
            "vishnu":0,
            "tom":120,
            "avinash":0,
            "jini":0,
            "asok":0
        }

        total_expense=sum(payment_summary.values())
        individual_split=total_expense/len(payment_summary)
        result={k:individual_split-v for k,v in payment_summary.items()}
        print(result)

sp=SpitWise()        
sp.solution()        
