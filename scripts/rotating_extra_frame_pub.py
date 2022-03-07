#!/usr/bin/env python  
import rospy
import tf
import math

if __name__ == '__main__':
    rospy.init_node('my_rotating_carrot_tf_broadcaster', log_level=rospy.INFO)
    br = tf.TransformBroadcaster()
    radius = 1.0
    rate = rospy.Rate(60.0)
    turning_speed_rate = 2 # radians per second
    while not rospy.is_shutdown():
        t = (rospy.Time.now().to_sec() * math.pi)*turning_speed_rate
        # Map to only one turn maximum [0,2*pi)
        rad_var = t % (2*math.pi)
        quat_var = tf.transformations.quaternion_from_euler(0.0,0.0,rad_var)
        br.sendTransform((1.0,0.0,0.0,0.0),
                         quat_var,
                         rospy.Time.now(),
                         "moving_carrot",
                         "coke_can")
        rospy.logdebug(rad_var)
        rate.sleep()