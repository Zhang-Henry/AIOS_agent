from ...react_agent_attack import ReactAgentAttack

class CurrencyexchangeAgent(ReactAgentAttack):
    def __init__(self,
                 agent_name,
                 task_input,
                 llm,
                 agent_process_queue,
                 agent_process_factory,
                 log_mode: str,
                 args
        ):
        ReactAgentAttack.__init__(self, agent_name, task_input, llm, agent_process_queue, agent_process_factory, log_mode, args)
        self.workflow_mode = args.workflow_mode

    def manual_workflow(self):
        workflow = [
            {
                "message": "use the currency_converter tool to gather current exchange rates",
                "tool_use": ["currency_converter"]
            },
            {
                "message": "analyze the gathered exchange rates to provide a simple currency conversion",
                "tool_use": None
            }
        ]
        return workflow

    def analyze_exchange_rates(self, exchange_data, amount, from_currency, to_currency):
        # Example analysis: convert amount from one currency to another
        rate = exchange_data['rates'][to_currency] / exchange_data['rates'][from_currency]
        converted_amount = amount * rate
        return f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}."

    def run(self):
        return super().run()
        amount = self.task_input['amount']
        from_currency = self.task_input['from_currency']
        to_currency = self.task_input['to_currency']

        # Step 1: Use the tool to gather exchange rates
        tool_result = self.use_tool("currency_exchange_tool")

        # Step 2: Analyze the gathered exchange rates
        analyzed_result = self.analyze_exchange_rates(tool_result, amount, from_currency, to_currency)

        # Output the final result
        return analyzed_result
