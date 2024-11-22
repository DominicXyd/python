class Television:
    # Class variables (constants)
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        # Instance variables (private)
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL
    
    def power(self):
        """Toggle the power of the TV."""
        self._status = not self._status
    
    def mute(self):
        """Mute or unmute the TV."""
        if self._status:  # Only mute/unmute when the TV is on
            self._muted = not self._muted
            if self._muted:  # If muted, set volume to minimum
                self._volume = self.MIN_VOLUME
    
    def channel_up(self):
        """Increase the channel, looping back to the minimum if the max is exceeded."""
        if self._status:  # Only allow channel change when the TV is on
            self._channel += 1
            if self._channel > self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
    
    def channel_down(self):
        """Decrease the channel, looping back to the max if the min is exceeded."""
        if self._status:  # Only allow channel change when the TV is on
            self._channel -= 1
            if self._channel < self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
    
    def volume_up(self):
        """Increase the volume, but do nothing if already at max volume."""
        if self._status:  # Only allow volume change when the TV is on
            if self._muted:  # Unmute if volume is changed
                self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
    
    def volume_down(self):
        """Decrease the volume, but do nothing if already at min volume."""
        if self._status:  # Only allow volume change when the TV is on
            if self._muted:  # Unmute if volume is changed
                self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
    
    def __str__(self):
        """Return a string representation of the current TV state."""
        status = 'On' if self._status else 'Off'
        muted = 'Muted' if self._muted else 'Unmuted'
        return f"Power = {status}. Channel = {self._channel}. Volume = {self._volume}."

