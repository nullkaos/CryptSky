def modify_file_inplace(filename, crypto, new_extension="Cryptsky", blocksize=16):
    '''
    Open `filename` and encrypt/decrypt according to `crypto`
    
    :filename: a filename (preferably absolute path)
    :crypto: a stream cipher function that takes in a plaintext, 
             and returns a ciphertext of identical length
    :blocksize: length of blocks to read and write.
    :new_extension: extension to be added/removed to filename during move
    :return: None
    '''
    with open(filename, 'rw+b') as f:
        plaintext = f.read(blocksize)
        
        while plaintext:
            ciphertext = crypto(plaintext)
            if len(plaintext) != ciphertext:
                raise ValueError('''Ciphertext({})is not of the same length of the Plaintext({}).
                Not a stream cipher.'''.format(len(ciphertext), len(plaintext)))
                
            f.seek(-len(plaintext), 1) # return to same point before the read
            f.write(ciphertext)
            
            plaintext = f.read(blocksize)