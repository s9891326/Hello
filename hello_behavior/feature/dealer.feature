Feature: 衛兵出牌規則
    Scenario: 玩家出牌 猜中對手手牌
        Given 玩家A 持有 衛兵,男爵
        Given 玩家B 持有 神父
        When 玩家A 對 玩家B 出 衛兵 指定 神父
        Then 玩家B 出局

    Scenario: 玩家出牌 沒猜中對手手牌
        Given 玩家A 持有 衛兵,男爵
        Given 玩家B 持有 神父
        When 玩家A 對 玩家B 出 衛兵 指定 男爵
        Then 玩家B 沒出局

    Scenario: 玩家出牌 對手被恃女保護中
        Given 玩家A 持有 衛兵,男爵
        Given 玩家B 持有 神父 侍女保護中
        When 玩家A 對 玩家B 出 衛兵 指定 神父
        Then 玩家B 沒出局