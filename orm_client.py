import odoorpc

class OdooClient:

    def __init__(self, config):

        self.odoo = odoorpc.ODOO(config['url'], port=config['port'])

        self.config = config
    
    def login(self):
        """[summary]

        Returns:
            [type]: [description]
        """        

        try:
            print('---------login initiated--------')

            response = self.odoo.login(
                self.config['db'], 
                self.config['user'], 
                self.config['password']
            )

            print('----------Login Successful--------')

            # return response 

        except Exception as error:

            return {
                'status_code':400,
                'status_message':'got an exception {}'.format(error)
            }
    
    def get_dbs(self):
        """[summary]

        Returns:
            [type]: [description]
        """        
        try:

            db_list = self.odoo.db.list()

            return db_list
        
        except Exception as error:

            return {
                'status_code':400,
                'status_message':'got an exception {}'.format(error)
            }
    
    def create(self, body):
        """[summary]

        Args:
            body ([type]): [description]

        Returns:
            [type]: [description]
        """        

        try:
            action = None

            if 'create' in body['action']:

                action = 'create'

            user = self.odoo.env.user

            print('---------model----------', body['model'])

            print('--------action------------', action)

            print('------------user_id-----------', [user.id])

            read_user_data = self.odoo.env['hr.employee'].create(
                { 
                    "create_uid": 4, 
                    "id": 11, 
                    "name": 'Ajay' 
                }
            )

            return read_user_data
        
        except Exception as error:

            return {
                'status_code':400,
                'status_message':'got an exception {}'.format(error)
            }
    
    def read(self, body):
        """[summary]

        Args:
            body ([type]): [description]

        Returns:
            [type]: [description]
        """        

        try:
            action = None

            print('------------body--------', body)

            if 'read' in body['action']:

                action = 'read'

            user = self.odoo.env.user

            print('---------model----------', body['model'])

            print('--------action------------', action)

            print('------------user_id-----------', [user.id])

            read_user_data = self.odoo.execute(body['model'], action, [user.id])

            return read_user_data
        
        except Exception as error:

            return {
                'status_code':400,
                'status_message':'got an exception {}'.format(error)
            }
    
    def update(self, body):
        """[summary]

        Args:
            body ([type]): [description]

        Returns:
            [type]: [description]
        """        

        try:
            action = None

            if 'action' in body and body['action'] == 'write':

                action = 'write'

            user = self.odoo.env.user

            update_user_data = self.odoo.env['hr.employee'].write(
                [user.id], {'name': "MyContact"}
            )

            return update_user_data
        
        except Exception as error:

            return {
                'status_code':400,
                'status_message':'got an exception {}'.format(error)
            }
    
    def delete(self, body):
        """[summary]

        Args:
            body ([type]): [description]

        Returns:
            [type]: [description]
        """        

        try:
            action = None

            if 'action' in body and body['action'] == 'unlink':

                action = 'unlink'

            user = self.odoo.env.user

            # read_user_data = self.odoo.execute(body['model'], action, [user.id])

            # return read_user_data

            delete_user_data = self.odoo.env['hr.employee'].unlink(
                [user.id]
            )

            return delete_user_data
        
        except Exception as error:

            return {
                'status_code':400,
                'status_message':'got an exception {}'.format(error)
            }
        
