#!/bin/bash

function createsshuser()
{
  USER="$1"
  shift
  SSH_PUBLIC_KEY="$*"

  # create a user with with password disabled but still logins possible with RSA key
  adduser --disabled-password --gecos ""  ${USER}

  # add the user to the wheel group so they can sudo
  usermod -a -G wheel ${USER}

  # add the ssh public key
  su - ${USER} -c "umask 022 ; mkdir .ssh ; ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa 2>/dev/null <<< y >/dev/null ; cat id_rsa.pub >> .ssh/authorised_keys"
}

createsshuser $1
