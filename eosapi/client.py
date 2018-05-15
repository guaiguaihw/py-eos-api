import time

from eosapi import HttpClient


class Client(HttpClient):
    def __init__(self, nodes=None, **kwargs):
        nodes = nodes or ['http://localhost:8888']
        super().__init__(nodes=nodes, **kwargs)

    def stream_blocks(self, start_block=None, mode='irreversible'):
        """ Stream raw blocks.

        Args:
             start_block (int): Block number to start streaming from. If None,
                                head block is used.
             mode (str): `irreversible` or `head`.
        """
        mode = 'last_irreversible_block_num' if mode == 'irreversible' \
            else 'head_block_num'

        # convert block id to block number
        if type(start_block) == str:
            start_block = int(start_block[:8], base=16)

        if not start_block:
            start_block = self.get_info()[mode]

        block_interval = 3  # todo: confirm this assumption trough api

        while True:
            head_block = self.get_info()[mode]
            for block_num in range(start_block, head_block + 1):
                yield self.get_block(block_num)
            start_block = head_block + 1
            time.sleep(block_interval)

    ##############################
    # apigen.py generated methods
    # below this point
    ##############################

    # ---------------------------
    # /v1/chain/*
    # ---------------------------
    def get_info(self) -> dict:
        """ Return general network information. """

        body = dict(
        )

        return self.exec(
            api='chain',
            endpoint='get_info',
            body=body
        )

    def get_block(self, block_num_or_id) -> dict:
        """ Fetch a block from the blockchain. """

        body = dict(
            block_num_or_id=block_num_or_id,
        )

        return self.exec(
            api='chain',
            endpoint='get_block',
            body=body
        )

    def get_account(self, name) -> dict:
        """ Fetch a blockchain account """

        body = dict(
            name=name,
        )

        return self.exec(
            api='chain',
            endpoint='get_account',
            body=body
        )

    # ---------------------------
    # /v1/history/*
    # ---------------------------
    def get_transaction(self, transaction_id) -> dict:
        """ Retrieve a transaction from the blockchain. """

        body = dict(
            id=transaction_id,
        )

        return self.exec(
            api='history',
            endpoint='get_transaction',
            body=body
        )

    def get_actions(self, account_name, pos, offset) -> dict:
        """ Retrieve all transactions with specific account name referenced in their scope. """

        body = dict(
            account_name=account_name,
            pos=pos,
            offset=offset,
        )

        return self.exec(
            api='history',
            endpoint='get_actions',
            body=body
        )

if __name__ == '__main__':
    client = Client(['http://localhost:8888'])
