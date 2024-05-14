from nes_py import NESEnv
import addresses

'''
print("X: " + str(self.ram[addresses.megamanXPos]))
print("Y: " + str(self.ram[addresses.megamanYPos]))
print("Sub X: " + str(self.ram[addresses.megamanSubXPos]))
print("Sub Y: " + str(self.ram[addresses.megamanSubYPos]))

'''

CAMERA_REWARD_MULTIPLYER = 10
POSITION_X_MULTIPLYER = 1
POSITION_Y_MULTIPLYER = 1


class MegamanEnv(NESEnv):
    """An OpenAI Gym interface to the NES game Megaman"""

    def __init__(self):
        """Initialize a new Megaman environment."""
        super(MegamanEnv, self).__init__('rom/test.nes')
        
        self.reset()

        self._backup()


    def _will_reset(self):
        """Handle any RAM hacking after a reset occurs."""
        # use this method to perform setup before and episode resets.
        # the method returns None
        print(self.ram)
    
    def _did_reset(self):
        """Handle any RAM hacking after a reset occurs."""
        # use this method to access the RAM of the emulator 
        # and perform setup for each episode. 
        # the method returns None
        pass

    def _did_step(self, done):
        """
        Handle any RAM hacking after a step occurs.

        Args:
            done: whether the done flag is set to true

        Returns:
            None

        """
        pass

    def _get_reward(self):
        """Return the reward after a step occurs."""
        
        return (CAMERA_REWARD_MULTIPLYER * self._camera_X_Screen) + (POSITION_X_MULTIPLYER * self._position_X) + ((POSITION_X_MULTIPLYER / 3) * self._position_Sub_X) + (POSITION_Y_MULTIPLYER * self._position_Y) + ((POSITION_Y_MULTIPLYER / 3) * self._position_Sub_Y)
    
    def _get_score(self):
        str_score = ""
        for a in addresses.score:
            b = self.ram[a]
            str_score += str(b)
        return int(str_score)    

    def _get_done(self):
        """Return True if the episode is over, False otherwise."""
        return False

    def _get_info(self):
        """Return the info after a step occurs."""
        return {}
    

    @property
    def _camera_X_Screen(self):
        return self.ram[addresses.CameraXScreen]
    
    @property
    def _position_Sub_X(self):
        return self.ram[addresses.megamanSubXPos]
    
    @property
    def _position_X(self):
        return self.ram[addresses.megamanXPos]
    
    @property
    def _position_Sub_Y(self):
        return self.ram[addresses.megamanSubYPos]
    
    @property
    def _position_Y(self):
        return self.ram[addresses.megamanYPos]


# explicitly define the outward facing API for the module
__all__ = [MegamanEnv.__name__]