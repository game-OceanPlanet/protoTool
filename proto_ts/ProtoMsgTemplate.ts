module qmr {
	/**
	 *
	 * @author coler 2018.12.11
	 * 根据消息MessageID自动生成，请勿修改
	 *
	 */
	export class ProtoMsgIdMap {
		private static _instance: ProtoMsgIdMap;
		public msgIdMap: any = {};

		/**
		*  获取单例
		*/
		public static get instance(): ProtoMsgIdMap {
			if (this._instance == null) { this._instance = new ProtoMsgIdMap(); }
			return this._instance;
		}

		public constructor() {
$params$
		}

	}
}
