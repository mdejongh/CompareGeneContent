import unittest
import os
import json
import time

from os import environ
from ConfigParser import ConfigParser
from pprint import pprint

from biokbase.workspace.client import Workspace as workspaceService
from biokbase.fbaModelServices.Client import fbaModelServices as fbaService
from CompareGeneContent.CompareGeneContentImpl import CompareGeneContent


class CompareGeneContentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        cls.ctx = {'token': token, 'provenance': [{'service': 'CompareGeneContent',
            'method': 'please_never_use_it_in_production', 'method_params': []}],
            'authenticated': 1}
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('CompareGeneContent'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = CompareGeneContent(cls.cfg)
        cls.fbaURL = cls.cfg['fba-url']
        cls.fbaClient = fbaService(cls.fbaURL, token=token)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getFBAClient(self):
        return self.__class__.fbaClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_CompareGeneContent_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_count_contigs(self):
        sbml = open("testmodel.xml").read()
        self.getFBAClient().import_fbamodel({'workspace':self.getWsName(), 'genome':'Rhodobacter_sphaeroides_2.4.1', 'genome_workspace':'KBaseExampleData', 'model':'model.1', 'biomass':'biomass0', 'sbml':sbml})
        matrix = {"data":{"col_ids":["r1"],"row_ids":["RSP_0002"],"values":[[0]]},"scale":"1.0","type":"log-ratio"}
        self.getWsClient().save_objects({'workspace': self.getWsName(), 'objects':
            [{'type': 'KBaseFeatureValues.ExpressionMatrix', 'name': 'matrix.1', 'data': matrix}]})
        ret = self.getImpl().compare_gene_content(self.getContext(), self.getWsName(), 'model.1', 'matrix.1')
        self.assertEqual(ret[0]['gene_intersection_count'],1)
        return ret
