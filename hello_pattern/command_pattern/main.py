from hello_pattern.command_pattern.cook_filet_steak_command import CookFiletSteakCommand
from hello_pattern.command_pattern.cook_sirloin_steak_command import CookSirloinSteakCommand
from hello_pattern.command_pattern.robot_chef_A import RobotChefA
from hello_pattern.command_pattern.robot_chef_B import RobotChefB


class Program:
    
    # first design
    def make_order1(self, order: list):
        result = []
        if "Filet Steak" in order:
            result.append("菲力牛排")
        
        if "Sirloin Steak" in order:
            result.append("沙朗牛排")
        
        return result
    
    # use command pattern
    def make_order2(self, order: list):
        cook_filet_steak = CookFiletSteakCommand(RobotChefA())
        cook_sirloin_steak = CookSirloinSteakCommand(RobotChefB())

        result = []
        if "Filet Steak" in order:
            result.append(cook_filet_steak.execute())

        if "Sirloin Steak" in order:
            result.append(cook_sirloin_steak.execute())

        return result


if __name__ == '__main__':
    orders = ["Filet Steak", "Sirloin Steak", "Steak"]
    # print(Program().make_order1(orders))
    print(Program().make_order2(orders))

