# -*- coding: utf-8 -*-
import threading
from threading import Condition

# 条件变量，用于复杂的线程同步

# 通过condition完成读诗

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        # type hints
        self.cond = cond  # type: Condition
        super().__init__(name='小爱')

    def run(self):
        with self.cond:
            self.cond.wait()
            print(f'{self.name} : 在')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name} : 好啊')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name} : 好啊')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name} : 好啊')
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        self.cond = cond  # type: Condition
        super().__init__(name='天猫精灵')

    def run(self):
        with self.cond:
            print(f'{self.name} : 小爱同学')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name} : 我们来对古诗吧')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name} : 我们来对古诗吧')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name} : 我们来对古诗吧')
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    lock = threading.Lock()
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    xiaoai.start()
    tianmao.start()

# condition由两层锁，一把底层锁会在线程调用了wait方法时候释放，上
# 面的锁会在每次调用wait的时候分配一把并放入conditon的等待队列当中，
# 等待notify方法的唤醒
    # tianmao.join()
    # xiaoai.join()
